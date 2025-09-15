import pygame, sys
from pygame.locals import *

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello World!")

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Fill the screen with a background color
    screen.fill((255, 255, 255)) # White

    # Render the "Hello World!" text
    font = pygame.font.SysFont("Arial", 48) # You can choose a different font and size
    text_surface = font.render("Hello World!", True, (0, 0, 0)) # Black text
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text_surface, text_rect)

    pygame.display.update()

pygame.quit()
sys.exit()

