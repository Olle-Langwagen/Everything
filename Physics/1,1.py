#Import pygame and sys
import pygame, sys
from pygame.locals import *

#Make a ball with gravity
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

#Set up pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Physics Engine")

#Start pygame
clock = pygame.time.Clock()
running = True

#Create a ball
ball = Ball(400, 0, 50, (255, 0, 0), 0.1)

#Main loop
while running:
    #Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    #Update ball
    ball.update()

    #Draw ball
    screen.fill((0, 0, 0))
    ball.draw(screen)

    #Update screen
    pygame.display.update()
    clock.tick(60)

#Quit pygame
pygame.quit()
sys.exit()

