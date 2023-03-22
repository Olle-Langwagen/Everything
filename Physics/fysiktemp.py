import pygame
import time
import sys

#Skärmskit
WIDTH = 640
HEIGHT = 480
FPS = 60

#Färger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

#Temperaturer
COLD_TEMP = 0
HOT_TEMP = 100

#Tid mellan varje uppdatering
TIME_INTERVAL = 100

class Material(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((35, 35))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.temperature = 25
        self.mass = 55
        self.density = 10
        self.dragging = False
        self.specific_heat_capacity = 0.1
        self.thermal_conductivity = 0.01

    def update(self, cold_area, hot_area):
        #Beräkna temperaturförändring baserat på om materialet är på en kall eller varm yta
        if self.rect.colliderect(cold_area.rect):
            heat_flow = self.thermal_conductivity * (COLD_TEMP - self.temperature) / self.rect.width * TIME_INTERVAL
            self.temperature += heat_flow / (self.mass * self.specific_heat_capacity)
        elif self.rect.colliderect(hot_area.rect):
            heat_flow = self.thermal_conductivity * (HOT_TEMP - self.temperature) / self.rect.width * TIME_INTERVAL
            self.temperature += heat_flow / (self.mass * self.specific_heat_capacity)
        #print(self.specific_heat_capacity, self.thermal_conductivity, self.mass)
    def draw_temperature(self, screen):
        #Rita ut materialets temperatur som en färg, alltså att den ändrar färg beroende på temperatur
        if self.temperature < COLD_TEMP:
            color = BLUE
        elif self.temperature > HOT_TEMP:
            color = RED
        else:
            color = (self.temperature * 2.55, 0, (100 - self.temperature) * 2.55)
        pygame.draw.rect(screen, color, self.rect)

        # Rita en border runt materialet
        border_rect = self.rect.inflate(0, 0)
        pygame.draw.rect(screen, BLACK, border_rect, 2)

    def draw_text(self, screen, font):
        #Skriv ut materialets temperatur
        text_surface = font.render("Temperatur: {:.1f}".format(self.temperature), True, BLACK)
        screen.blit(text_surface, (10, 30))
    

# Subklasser av klassen Material
class CopperMaterial(Material):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill((184, 115, 51))  # Färg som motsvarar koppar
        self.mass = 8.96 * 10 ** 3  # Densitet (kg/m^3) av koppar
        self.thermal_conductivity = 385  # Termisk konduktivitet (W/(m*K)) av koppar
        self.specific_heat_capacity = 385  # Specifik värmekapacitet (J/(kg*K)) av koppar


class IronMaterial(Material):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill((144, 91, 61))  # Färg som motsvarar järn
        self.mass = 7.87 * 10 ** 3  # Densitet (kg/m^3) av järn
        self.thermal_conductivity = 80.2  # Termisk konduktivitet (W/(m*K)) av järn
        self.specific_heat_capacity = 450  # Specifik värmekapacitet (J/(kg*K)) av järn


class GoldMaterial(Material):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill(WHITE)  # Färg som motsvarar guld
        self.mass = 19.3 * 10 ** 3  # Densitet (kg/m^3) av guld
        self.thermal_conductivity = 318  # Termisk konduktivitet (W/(m*K)) av guld
        self.specific_heat_capacity = 129  # Specifik värmekapacitet (J/(kg*K)) av guld







class Area(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Timer:
    def __init__(self):
        self.start_time = time.time()

    def get_time(self):
        # Beräkna tiden som gått sedan starten
        return time.time() - self.start_time

    def draw_text(self, screen, font):
        # Rita ut tiden som gått som text
        text_surface = font.render("Tid: {:.1f}".format(self.get_time()), True, BLACK)
        screen.blit(text_surface, (10, 10))

def show_menu(screen, font):

    screen.fill(WHITE)

    # Skapa textobjekt för menyalternativen
    title_text = font.render("Temperatur Simulation", True, BLACK)
    start_text = font.render("Starta Spelet (Tryck Space)", True, BLACK)
    quit_text = font.render("Avsluta (Tryck ESC)", True, BLACK)

    # Bestäm position för textobjekten
    title_rect = title_text.get_rect(center=(320, 100))
    start_rect = start_text.get_rect(center=(320, 200))
    quit_rect = quit_text.get_rect(center=(320, 300))

    # Rita textobjekten på skärmen
    screen.blit(title_text, title_rect)
    screen.blit(start_text, start_rect)
    screen.blit(quit_text, quit_rect)

    pygame.display.flip()

    # Loopa tills användaren väljer ett alternativ
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    return "start"

def show_material_menu(screen, font):

    global material
    screen.fill(WHITE)


    # Skapa textobjekt för menyalternativen
    title_text = font.render("Välj material", True, BLACK)
    Koppar_text = font.render("Koppar (Tryck 1)", True, BLACK)
    järn_text = font.render("Järn (Tryck 2)", True, BLACK)
    guld_text = font.render("Guld (Tryck 3)", True, BLACK)

    # Bestäm position för textobjekten
    title_rect = title_text.get_rect(center=(320, 100))
    material1_rect = Koppar_text.get_rect(center=(320, 150))
    material2_rect = järn_text.get_rect(center=(320, 200))
    material3_rect = guld_text.get_rect(center=(320, 250))

    # Rita textobjekten på skärmen
    screen.blit(title_text, title_rect)
    screen.blit(Koppar_text, material1_rect)
    screen.blit(järn_text, material2_rect)
    screen.blit(guld_text, material3_rect)

    pygame.display.flip()

    # Loopa tills användaren väljer ett alternativ
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_1:
                    print("Koppar valt")
                    
                    return "material1"
                elif event.key == pygame.K_2:
                    print("Järn valt")

                    return "material2"
                elif event.key == pygame.K_3:
                    print("Guld valt")

                    return "material3"
    

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Temperature Simulation")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 24)
    # Visa meny för materialval
    material_choice = show_material_menu(screen, font)
    if material_choice == "material1":
        print("Koppar valt")
        material = CopperMaterial(320, 240)
    elif material_choice == "material2":
        print("Järn valt")
        material = IronMaterial(320, 240)
    elif material_choice == "material3":
        print("Guld valt")
        material = GoldMaterial(320, 240)
    else:
        # Standardmaterial om inget valdes
        material = Material(320, 240)
    # Visa menyn
    choice = show_menu(screen, font)

    # Starta spelet om användaren valde att starta
    if choice == "start":
        # Skapa två ytor, en kall och en varm
        cold_area = Area(50, 50, 200, 200, BLUE)
        hot_area = Area(390, 50, 200, 200, RED)

        # Skapa en timer för att räkna tiden
        timer = Timer()

        all_sprites = pygame.sprite.Group()
        all_sprites.add(cold_area, hot_area, material)
        
        running = True
        while running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Kontrollera om användaren klickade på materialet med vänster musknapp
                    if event.button == 1 and material.rect.collidepoint(event.pos):
                        # Sätt dragging-flaggan till True
                        material.dragging = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    # Sätt dragging-flaggan till False när användaren släpper vänster musknapp
                    if event.button == 1:
                        material.dragging = False
                elif event.type == pygame.MOUSEMOTION:
                    # Flytta materialet med musen när användaren drar materialet
                    if material.dragging:
                        material.rect.move_ip(event.rel)

            # Uppdatera materialets temperatur baserat på vilken yta den befinner sig på
            material.update(cold_area, hot_area)

            # Rita allt på skärmen
            screen.fill(WHITE)
            all_sprites.draw(screen)
            material.draw_temperature(screen)
            material.draw_text(screen, font)
            timer.draw_text(screen, font)

            pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
    main()