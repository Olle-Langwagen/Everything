import pygame
import numpy as np

# Set up the constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
HEAT_TRANSFER_RATE = 0.01
THERMAL_CONDUCTIVITY = 1
HEAT_CAPACITY = 1
DENSITY = 1

# Set up the hot and cold spots
hot_spot = pygame.Rect(0, HEIGHT // 2 - 50, 50, 100)
hot_spot_temperature = 100
cold_spot = pygame.Rect(WIDTH - 50, HEIGHT // 2 - 50, 50, 100)
cold_spot_temperature = 0

# Set up the material
material = pygame.Rect(WIDTH // 2 - 25, HEIGHT // 2 - 25, 50, 50)
material_temperature = 50

# Set up the heat equation
num_points = 100
x = np.linspace(0, WIDTH, num_points)
dx = x[1] - x[0]
dt = 0.01
alpha = THERMAL_CONDUCTIVITY / (DENSITY * HEAT_CAPACITY)
T = np.ones(num_points) * material_temperature
T[int(material.left // dx) : int(material.right // dx)] = material_temperature


# Set up the pygame window
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Temperature Simulation")
clock = pygame.time.Clock()

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                material.move_ip(-20, 0)
            elif event.key == pygame.K_RIGHT:
                material.move_ip(20, 0)
            elif event.key == pygame.K_UP:
                material.move_ip(0, -20)
            elif event.key == pygame.K_DOWN:
                material.move_ip(0, 20)

    # Update the temperature of the material based on the heat equation
    if material.colliderect(hot_spot) or material.colliderect(cold_spot):
        T[int(material.left // dx) : int(material.right // dx)] = material_temperature
        T[0] = hot_spot_temperature
        T[-1] = cold_spot_temperature
        T[1:-1] += alpha * dt / dx**2 * (T[2:] - 2 * T[1:-1] + T[:-2])
        material_temperature = T[int(material.centerx // dx)]

        # Calculate the temperature difference between the material and the hot and cold spots
        hot_spot_distance = abs(hot_spot.centerx - material.centerx)
        cold_spot_distance = abs(cold_spot.centerx - material.centerx)
        temperature_diff = hot_spot_temperature - cold_spot_temperature

        # Calculate the heat transfer rate
        if hot_spot_distance < cold_spot_distance:
            heat_transfer_rate = (hot_spot_temperature - material_temperature) * HEAT_TRANSFER_RATE * hot_spot.width
        else:
            heat_transfer_rate = (cold_spot_temperature - material_temperature) * HEAT_TRANSFER_RATE * cold_spot.width

        # Update the temperature of the material
        material_temperature += heat_transfer_rate*dt
        material_temperature = max(cold_spot_temperature, min(hot_spot_temperature, material_temperature))
    # Clear the screen
    win.fill(WHITE)

    # Draw the hot and cold spots
    pygame.draw.rect(win, RED, hot_spot)
    pygame.draw.rect(win, BLUE, cold_spot)

    # Draw the material with a color based on its temperature
    color = (int(max(0, min(255, material_temperature / 100 * 255))),
            int(max(0, min(255, (1 - material_temperature / 100) * 255))), 0)
    pygame.draw.rect(win, color, material)

    # Display the temperature on the screen
    font = pygame.font.SysFont(None, 50)
    text = font.render("Temperature: {:.1f} C".format(material_temperature), True, BLACK)
    text_rect = text.get_rect()
    text_rect.topleft = (10, 10)
    win.blit(text, text_rect)

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)
pygame.quit()