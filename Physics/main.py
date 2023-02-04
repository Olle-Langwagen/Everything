import math
import pygame

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

#Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Physics Engine")
    clock = pygame.time.Clock()
    running = True

    #Create physics engine
    physics = PhysicsEngine(0.5, 0.9)

    #Create physics object
    physicsObject = PhysicsObject([100, 100], [0, 0], 1)
    physics.add(physicsObject)

    #Create pygame engine
    pygameEngine = PygameEngine(screen)

    #Create pygame object
    pygameObject = PygameObject([100, 100], [0, 0], 1, pygame.image.load("Physics/ball.png"))
    pygameEngine.add(pygameObject)

    #Main loop
    while running:
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Update physics engine
        physics.update()

        #Update pygame engine
        pygameEngine.update()

        #Update screen
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()