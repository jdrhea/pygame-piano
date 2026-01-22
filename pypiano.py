import pygame
from sys import exit
from itertools import chain

pygame.init()
pygame.mixer.init()

GAME_WIDTH = 1300
GAME_HEIGHT = 600

SPACE_WIDTH = 5

KEY_WIDTH = (GAME_WIDTH / 14)-SPACE_WIDTH
KEY_HEIGHT = 250

whiteKeyLabels = ["C1", "D1", "E1", "F1", "G1", "A1", "B1", "C2", "D2", "E2", "F2", "G2", "A2", "B2"]
blackKeyLabels = ["C#1", "D#1","", "F#1", "G#1", "A#1","", "C#2", "D#2","", "F#2", "G#2", "A#2", ""]


pygame.init()    
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption('Pygame Piano')
clock = pygame.time.Clock()



def draw():
    for i in range(0, 14):
        key = pygame.Rect((KEY_WIDTH + SPACE_WIDTH) * i , GAME_HEIGHT - KEY_HEIGHT, KEY_WIDTH, KEY_HEIGHT)
        pygame.draw.rect(window, (255, 255, 255), key)  # key fill
        key_font = pygame.font.SysFont('Gill Sans', 25)
        key_text = key_font.render(whiteKeyLabels[i], True, 'gray')
        window.blit(key_text, (i * (KEY_WIDTH + SPACE_WIDTH) + KEY_WIDTH/2, KEY_HEIGHT *2))
    for i in chain(range(0, 2), range(3, 6), range(7,9), range(10,13)):
        blackKey = pygame.Rect(3/4*KEY_WIDTH + (KEY_WIDTH + SPACE_WIDTH)*i, GAME_HEIGHT - KEY_HEIGHT, KEY_WIDTH/2, KEY_HEIGHT/2)
        pygame.draw.rect(window, (50, 50, 50), blackKey)  # key fill
        blackKey_font = pygame.font.SysFont('Gill Sans', 24)
        key_text = blackKey_font.render(blackKeyLabels[i], True, 'gray')
        window.blit(key_text, (3/4*KEY_WIDTH + (KEY_WIDTH + SPACE_WIDTH)*i, KEY_HEIGHT+KEY_HEIGHT/2))

while True: # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if click X button on window
            pygame.quit()
            exit()

    draw()
    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 FPS