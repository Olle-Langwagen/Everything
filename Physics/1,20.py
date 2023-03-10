import pygame
import time

pygame.init()

cold_color = (0, 0, 255)
hot_color = (255, 0, 0)

window_size = (800, 600)
cold_surface = pygame.Surface((150, 150))
cold_surface.fill(cold_color)
hot_surface = pygame.Surface((150, 150))
hot_surface.fill(hot_color)

class Material:
    def __init__(self, surface, x, y, temperature, conductivity):
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.temperature = temperature
        self.conductivity = conductivity

def update_cold_surface(material, delta_time):
    global COLD_TEMP
    temperature_diff = material.temperature - COLD_TEMP
    heat_transfer = material.conductivity * temperature_diff * delta_time
    material.temperature -= heat_transfer
    cold_surface.fill((cold_color[0], cold_color[1], int(COLD_TEMP)))

def update_hot_surface(material, delta_time):
    global HOT_TEMP
    temperature_diff = HOT_TEMP - material.temperature
    heat_transfer = material.conductivity * temperature_diff * delta_time
    material.temperature += heat_transfer
    hot_surface.fill((hot_color[0], hot_color[1], int(HOT_TEMP)))

def update_material(material, delta_time):
    global COLD_TEMP, HOT_TEMP

    # Kolla om materialet kolliderar med den kalla ytan
    cold_collision = material.rect.colliderect(cold_surface.get_rect())

    # Kolla om materialet kolliderar med den varma ytan
    hot_collision = material.rect.colliderect(hot_surface.get_rect())

    # Om materialet kolliderar med den kalla ytan
    if cold_collision:
        material.temperature -= delta_time * material.conductivity * (material.temperature - COLD_TEMP)

    # Om materialet kolliderar med den varma ytan
    elif hot_collision:
        material.temperature += delta_time * material.conductivity * (HOT_TEMP - material.temperature)

def draw(surface, material):
    global COLD_TEMP, HOT_TEMP

    surface.blit(cold_surface, (50, 100))
    surface.blit(hot_surface, (600, 100))
    surface.blit(material.surface, material.rect)

    font = pygame.font.Font(None, 36)
    cold_text = font.render(f"Cold Surface: {COLD_TEMP:.2f} C", True, (255, 255, 255))
    hot_text = font.render(f"Hot Surface: {HOT_TEMP:.2f} C", True, (255, 255, 255))
    material_text = font.render(f"Material: {material.temperature:.2f} C", True, (255, 255, 255))
    time_text = font.render(time.strftime('%H:%M:%S'), True, (255, 255, 255))

    surface.blit(cold_text, (50, 50))
    surface.blit(hot_text, (600, 50))
    surface.blit(material_text, (material.rect.x + 10, material.rect.y + 10))
    surface.blit(time_text, (window_size[0] - 150, 50))
def run_game():
    global COLD_TEMP, HOT_TEMP

    material_surface = pygame.Surface((50, 50))
    material_surface.fill((255, 255, 255))
    material = Material(material_surface, 375, 275, 25, 0.1)
    delta_time = 0.1

    screen = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()

    is_dragging = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and material.rect.collidepoint(event.pos):
                    is_dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if is_dragging:
                    material.rect.move_ip(event.rel)

        update_cold_surface(material, delta_time)
        update_hot_surface(material, delta_time)
        update_material(material, delta_time)

        screen.fill((0, 0, 0))
        draw(screen, material)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    COLD_TEMP = 59.0
    HOT_TEMP = 95.0
    run_game()