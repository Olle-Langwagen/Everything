import pygame
import sys
from pygame.locals import *
import math

# Description: A ball that has buoyancy

#physics simulation with a ball that has buoyancy, there should be water, you should be able to change mass and buyancy

#Basic physics engine
class PhysicsEngine:
    def __init__(self, gravity, friction):
        self.gravity = gravity
        self.friction = friction
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def update(self):
        for object in self.objects:
            object.velocity[1] += self.gravity
            object.velocity[0] *= self.friction
            object.velocity[1] *= self.friction
            object.position[0] += object.velocity[0]
            object.position[1] += object.velocity[1]

#Basic physics object
class PhysicsObject:
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass

#Basic pygame object
class PygameObject:
    def __init__(self, position, velocity, mass, image):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, self.position)

#Basic pygame engine
class PygameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def update(self):
        for object in self.objects:
            object.draw(self.screen)

#Ball with buoyancy
class BuoyantBall:
    def __init__(self, position, velocity, mass, image, buoyancy):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.image = image
        self.buoyancy = buoyancy

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def update(self):
        self.velocity[1] += self.buoyancy
        self.velocity[0] *= 0.99
        self.velocity[1] *= 0.99
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

#Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Physics Engine")
    clock = pygame.time.Clock()
    running = True
    ball = BuoyantBall([100, 100], [0, 0], 10, pygame.image.load("Physics/ball.png"), 0.1)
    pygameEngine = PygameEngine(screen)
    pygameEngine.add(ball)
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygameEngine.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()