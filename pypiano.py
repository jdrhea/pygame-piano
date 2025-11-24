import pygame
from sys import exit

pygame.init()
pygame.mixer.init()

GAME_WIDTH = 1300
GAME_HEIGHT = 600

KEY_WIDTH = 50
KEY_HEIGHT = 200

pygame.init()    
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption('Pygame Piano')
clock = pygame.time.Clock()

key = pygame.Rect(0, GAME_HEIGHT - KEY_HEIGHT, KEY_WIDTH, KEY_HEIGHT)

def draw():
    for i in range(1, 13):
        pygame.draw.rect(window, (255, 255, 255), key)

while True: # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if click X button on window
            pygame.quit()
            exit()

    draw()
    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 FPS