import pygame
import sys
from pygame.locals import *
import math


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


class PhysicsObject:
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass


class PygameObject:
    def __init__(self, position, velocity, mass, image):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, self.position)


class PygameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def update(self):
        for object in self.objects:
            object.draw(self.screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Physics Engine")
    clock = pygame.time.Clock()
    running = True

    #Create physics engine
    physics = PhysicsEngine(0.1, 0.99)

    #Create pygame engine
    pygame_engine = PygameEngine(screen)

    #Create ball
    ball = PhysicsObject([400, 0], [0, 0], 1)
    ball_image = pygame.image.load("Physics/ball.png")
    ball_image = pygame.transform.scale(ball_image, (100, 100))
    pygame_ball = PygameObject(ball.position, ball.velocity, ball.mass, ball_image)
    physics.add(ball)
    pygame_engine.add(pygame_ball)

    #Main loop
    while running:
        #Check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        #Update physics
        physics.update()

        #Update pygame
        screen.fill((0, 0, 0))
        pygame_engine.update()

        #Update screen
        pygame.display.update()
        clock.tick(10)

    #Quit pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

