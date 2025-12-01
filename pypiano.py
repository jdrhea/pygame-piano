import pygame
from sys import exit

pygame.init()
pygame.mixer.init()

GAME_WIDTH = 1300
GAME_HEIGHT = 600

SPACE_WIDTH = 10

KEY_WIDTH = (GAME_WIDTH / 14)-SPACE_WIDTH
KEY_HEIGHT = 250

keyLabels = {"C1", "D1", "E1", "F1", "G1", "A1", "B1", "C2", "D2", "E2", "F2", "G2", "A2", "B2"}


pygame.init()    
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption('Pygame Piano')
clock = pygame.time.Clock()



def draw():
    for i in range(0, 14):
        key = pygame.Rect(0 + (KEY_WIDTH + SPACE_WIDTH) * i , GAME_HEIGHT - KEY_HEIGHT, KEY_WIDTH, KEY_HEIGHT)
        pygame.draw.rect(window, (255, 255, 255), key)  # key fill
        key_font = pygame.font.SysFont('Gill Sans', 25)
        key_text = key_font.render("C", True, (175, 175, 175))
        window.blit(key_text, (i * (KEY_WIDTH + SPACE_WIDTH) + KEY_WIDTH/2, KEY_HEIGHT *2))

while True: # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if click X button on window
            pygame.quit()
            exit()

    draw()
    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 FPS