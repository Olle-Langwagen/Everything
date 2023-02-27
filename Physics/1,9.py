import pygame

# Set up the window
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Temperature Simulation")
clock = pygame.time.Clock()

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

hot_spot_temperature = 100.0  # in degrees Celsius
cold_spot_temperature = 0.0  # in degrees Celsius

# Set up the hot and cold spots
hot_spot = pygame.Rect(WIDTH - 100, HEIGHT // 2 - 50, 50, 100)
cold_spot = pygame.Rect(50, HEIGHT // 2 - 50, 50, 100)

# Set up the material
material = pygame.Rect(WIDTH // 2 - 25, HEIGHT // 2 - 25, 50, 50)
mass = 1.0  # in kilograms
specific_heat = 0.2  # in joules per gram-degree Celsius
temperature = 25.0  # in degrees Celsius

# Set up the temperature model
thermal_conductivity = 1.0  # in watts per meter-degree Celsius
def calculate_temperature():
    global temperature
    dist_to_hot = abs(hot_spot.centerx - material.centerx)
    dist_to_cold = abs(cold_spot.centerx - material.centerx)
    rate_of_heat_transfer = (thermal_conductivity * material.width * material.height *
                             (hot_spot_temperature - cold_spot_temperature) /
                             (dist_to_hot + dist_to_cold))
    delta_T = rate_of_heat_transfer / (mass * specific_heat)
    temperature += delta_T

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the material with the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        material.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        material.move_ip(5, 0)
    if keys[pygame.K_UP]:
        material.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        material.move_ip(0, 5)

   
    # Calculate the temperature
    calculate_temperature()

    # Draw the hot and cold spots
    pygame.draw.rect(win, RED, hot_spot)
    pygame.draw.rect(win, BLUE, cold_spot)

    # Draw the material with a color based on its temperature
    color = (temperature / 100 * 255, (1 - temperature / 100) * 255, 0)
    pygame.draw.rect(win, color, material)

    # Display the temperature on the screen
    font = pygame.font.SysFont(None, 30)
    text = font.render("Temperature: {:.1f} C".format(temperature), True, WHITE)
    win.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit the program
pygame.quit()
