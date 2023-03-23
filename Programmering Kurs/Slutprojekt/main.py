import time
import pygame

# This is a 2D platformer game. The player can move left and right, jump.
pygame.display.set_caption("Platformer")
# Set up the pygame window
pygame.init()
SCREENWIDTH, SCREENHEIGHT = 1000, 600
window = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
bg = pygame.image.load("Programmering Kurs/Slutprojekt/Images/BG.jpeg")




# Player class

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("Programmering Kurs/Slutprojekt/Images/player.png")
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y


Player(100, 10)
# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Quit if player hits the escape key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            

    window.blit(bg, (0, 0))
    pygame.display.update()

pygame.quit()


