import pygame, sys
from pygame.locals import *

class Ball:
    def __init__(self, x, y, radius, color, gravity):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.gravity = gravity
        self.velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        #Check for collision with ramp
        slope = (600 - 450) / (150)
        y_intercept = 600 - slope * 150
        y_val = slope * self.x + y_intercept
        if self.y + self.radius >= y_val and self.x - self.radius <= 150:
            self.velocity = -self.velocity
            self.y = max(self.y, y_val - self.radius)

        #Check for collision with bottom rectangle
        if self.y + self.radius >= 550 and self.x + self.radius >= 100 and self.x - self.radius <= 300:
            self.velocity = -self.velocity
            self.y = 550 - self.radius


#Set up pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Physics Engine")

#Start pygame
clock = pygame.time.Clock()
running = True

#Create a ball
ball = Ball(100, 100, 50, (60, 100, 100), 0.1)

#Main loop
while running:
    #Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    #Update ball
    ball.update()

    #Draw ball and ramp
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (300, 550, 200, 50))
    pygame.draw.polygon(screen, (255, 255, 255), [(0,600),(150,600),(0,450)])
    ball.draw(screen)

    #Update screen
    pygame.display.update()
    clock.tick(60)

#Quit pygame
pygame.quit()
sys.exit()
