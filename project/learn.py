import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("RPG Chess")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill("Red")
image_surface = pygame.image.load("project/graphics/flop.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(image_surface, (0, 0)) #blit = block image transfer
    
    pygame.display.update()
    clock.tick(60)