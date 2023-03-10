import pygame

# Definiera initiala parametrar
material_temp = 293  # K
hot_surface_temp = 980  # K
cold_surface_temp = -100002  # K
hot_surface_area = 0.01  # m^2
cold_surface_area = 0.1  # m^2

# Definiera materialen
material_1 = {
    "name": "Aluminium",
    "density": 2700,  # kg/m^3
    "specific_heat_capacity": 910,  # J/(kg*K)
    "thermal_conductivity": 205,  # W/(m*K)
    "heat_transfer_coefficient": 100  # W/(m^2*K)
}

material_2 = {
    "name": "Koppar",
    "density": 899,  # kg/m^3
    "specific_heat_capacity": 386,  # J/(kg*K)
    "thermal_conductivity": 401,  # W/(m*K)
    "heat_transfer_coefficient": 100  # W/(m^2*K)
}

# Funktion för att beräkna materialets temperatur när det är på en yta
def calculate_material_temperature(material, surface_temp, surface_area, initial_material_temp, time_on_surface, time_step):
    mass = material["density"] * surface_area * 0.001  # Massa (kg) = densitet (kg/m^3) * area (m^2) * tjocklek (m)
    energy_transfer_rate = material["heat_transfer_coefficient"] * surface_area * (surface_temp - initial_material_temp)  # Energiöverföringshastighet (W) = värmeöverföringskoefficient (W/(m^2*K)) * area (m^2) * temperaturskillnad (K)
    energy_transfer = energy_transfer_rate * time_step  # Energiöverföring (J) = energiöverföringshastighet (W) * tid (s)
    energy_change = material["specific_heat_capacity"] * mass * (surface_temp - initial_material_temp)  # Energiförändring (J) = specifik värmekapacitet (J/(kg*K)) * massa (kg) * temperaturskillnad (K)
    final_temp = initial_material_temp + (energy_transfer + energy_change) / (material["specific_heat_capacity"] * mass)  # Slutlig temperatur (K) = initial temperatur (K) + (energiöverföring (J) + energiförändring (J)) / (specifik värmekapacitet (J/(kg*K)) * massa (kg))
    return final_temp

# Initera Pygame
pygame.init()

# Definiera fönstrets storlek
win_size = win_width, win_height = 800, 600

# Skapa fönstret
win = pygame.display.set_mode(win_size)

# Skapa klockan för att hålla tid
clock = pygame.time.Clock()

# Skapa rektangeln för materialet
material_rect = pygame.Rect(0, 0, 50, 50)
material_rect.center = win_width // 2, win_height // 2

# Skapa textobjekt för att visa materialets temperatur
font = pygame.font.Font(None, 30)
temp_text = font.render("Materialtemperatur: {} K".format(material_temp), True, (255, 255, 255))
temp_text_rect = temp_text.get_rect()
temp_text_rect.bottomleft = (10, win_height - 10)

# Skapa linjer för den varma och kalla ytan
hot_surface_line = pygame.Rect(0, 0, win_width, 50)
hot_surface_color = (255, 0, 0)
cold_surface_line = pygame.Rect(0, win_height - 50, win_width, 50)
cold_surface_color = (0, 0, 255)

dragging_material = False

time_on_hot_surface = 0
time_on_cold_surface = 0

energy_to_add = 0
energy_to_remove = 0

heat_transfer_time = 0.5 # sekunder

while True:
    # Hantera händelser
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and material_rect.collidepoint(event.pos):
                # Användaren börjar dra materialet
                dragging_material = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                # Användaren slutar dra materialet
                dragging_material = False
                time_on_hot_surface = 0
                time_on_cold_surface = 0
        # Uppdatera materialets position och temperatur om användaren drar materialet
    if dragging_material:
        material_rect.center = pygame.mouse.get_pos()
        if material_rect.colliderect(hot_surface_line):
            time_on_hot_surface += clock.get_time() / 1000
            energy_to_add += material_1["heat_transfer_coefficient"] * hot_surface_area * (hot_surface_temp - material_temp) * (clock.get_time() / 1000)
        elif material_rect.colliderect(cold_surface_line):
            time_on_cold_surface += clock.get_time() / 1000
            energy_to_remove += material_2["heat_transfer_coefficient"] * cold_surface_area * (material_temp - cold_surface_temp) * (clock.get_time() / 1000)
        temp_text = font.render("Materialtemperatur: {} K".format(round(material_temp, 2)), True, (255, 255, 255))

    if energy_to_add > 0:
        energy_to_remove = 0
        time_on_cold_surface = 0
        time_on_hot_surface += clock.get_time() / 1000
        energy_added = min(energy_to_add, material_1["specific_heat_capacity"] * material_1["density"] * hot_surface_area * (hot_surface_temp - material_temp) * heat_transfer_time)
        material_temp += energy_added / (material_1["specific_heat_capacity"] * material_1["density"] * hot_surface_area)
        energy_to_add -= energy_added
    elif energy_to_remove > 0:
        energy_to_add = 0
        time_on_hot_surface = 0
        time_on_cold_surface += clock.get_time() / 1000
        energy_removed = min(energy_to_remove, material_2["specific_heat_capacity"] * material_2["density"] * cold_surface_area * (material_temp - cold_surface_temp) * heat_transfer_time)
        material_temp -= energy_removed / (material_2["specific_heat_capacity"] * material_2["density"] * cold_surface_area)
        energy_to_remove -= energy_removed
    else:
        time_on_hot_surface = 0
        time_on_cold_surface = 0

    # Rita allt på skärmen
    win.fill((0, 0, 0))
    pygame.draw.rect(win, hot_surface_color, hot_surface_line)
    pygame.draw.rect(win, cold_surface_color, cold_surface_line)
    pygame.draw.rect(win, (0, 255, 0), material_rect)
    win.blit(temp_text, temp_text_rect)

    # Uppdatera skärmen
    pygame.display.update()

    # Håll klockan uppdaterad
    clock.tick(60)
