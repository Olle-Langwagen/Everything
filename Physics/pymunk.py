import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elastic Collisions")

# Define objects
class Object:
    def __init__(self, x, y, size, color, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        
    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        
        # Check for collision with walls
        if self.x - self.size/2 <= 0 or self.x + self.size/2 >= WIDTH:
            self.x_velocity *= -1
        if self.y - self.size/2 <= 0 or self.y + self.size/2 >= HEIGHT:
            self.y_velocity *= -1
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.size)
        
    def check_collision(self, other):
        # Calculate distance between centers of objects
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        
        # Check if distance is less than sum of radii (collision)
        if distance <= self.size/2 + other.size/2:
            # Calculate angle of collision
            angle = math.atan2(other.y - self.y, other.x - self.x)
            
            # Calculate velocity components along and perpendicular to angle of collision
            self_velocity_x = self.x_velocity * math.cos(angle) + self.y_velocity * math.sin(angle)
            self_velocity_y = self.y_velocity * math.cos(angle) - self.x_velocity * math.sin(angle)
            other_velocity_x = other.x_velocity * math.cos(angle) + other.y_velocity * math.sin(angle)
            other_velocity_y = other.y_velocity * math.cos(angle) - other.x_velocity * math.sin(angle)
            
            # Calculate new velocities along angle of collision (conserving momentum and kinetic energy)
            self_velocity_x, other_velocity_x = other_velocity_x, self_velocity_x
            
            # Calculate new x and y velocity components
            self.x_velocity = self_velocity_x * math.cos(angle) - self_velocity_y * math.sin(angle)   
            self.y_velocity = self_velocity_y * math.cos(angle) - self_velocity_x * math.sin(angle)
            other.x_velocity = other_velocity_x * math.cos(angle) - other_velocity_y * math.sin(angle)
            other.y_velocity = other_velocity_y * math.cos(angle) + other_velocity_x * math.sin(angle)

# Create objects
object1 = Object(100, 100, 50, (255, 0, 0), 2, 3)
object2 = Object(400, 400, 30, (0, 255, 0), -2, -3)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Clear window
    window.fill((255, 255, 255))
    
    # Update and draw objects
    object1.update()
    object1.draw(window)
    object2.update()
    object2.draw(window)
    
    # Check for collision
    object1.check_collision(object2)
    
    # Update display
    pygame.display.update()
    
    # Slow down the program
    pygame.time.delay(0)  # 60 FPS

# Quit Pygame
pygame.quit()
