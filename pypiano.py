import pygame
from sys import exit
from itertools import chain
import time

pygame.init()
pygame.mixer.init()

GAME_WIDTH = 1300
GAME_HEIGHT = 600

SPACE_WIDTH = 5

KEY_WIDTH = (GAME_WIDTH / 14)-SPACE_WIDTH
KEY_HEIGHT = 250

whiteKeyLabels = ["C1", "D1", "E1", "F1", "G1", "A1", "B1", "C2", "D2", "E2", "F2", "G2", "A2", "B2"]
blackKeyLabels = ["C#1", "D#1","", "F#1", "G#1", "A#1","", "C#2", "D#2","", "F#2", "G#2", "A#2", ""]

C1sound = pygame.mixer.Sound("C1.mp3")
Csharp1sound = pygame.mixer.Sound("C#1.mp3")
D1sound = pygame.mixer.Sound("D1.mp3")
Dsharp1sound = pygame.mixer.Sound("D#1.mp3")
E1sound = pygame.mixer.Sound("E1.mp3")
F1sound = pygame.mixer.Sound("F1.mp3")
Fsharp1sound = pygame.mixer.Sound("F#1.mp3")
G1sound = pygame.mixer.Sound("G1.mp3")
Gsharp1sound = pygame.mixer.Sound("G#1.mp3")
A1sound = pygame.mixer.Sound("A1.mp3")
Asharp1sound = pygame.mixer.Sound("A#1.mp3")
B1sound = pygame.mixer.Sound("B1.mp3")
C2sound = pygame.mixer.Sound("C2.mp3")
Csharp2sound = pygame.mixer.Sound("C#2.mp3")
D2sound = pygame.mixer.Sound("D2.mp3")
Dsharp2sound = pygame.mixer.Sound("D#2.mp3")
E2sound = pygame.mixer.Sound("E2.mp3")
F2sound = pygame.mixer.Sound("F2.mp3")
Fsharp2sound = pygame.mixer.Sound("F#2.mp3")
G2sound = pygame.mixer.Sound("G2.mp3")
Gsharp2sound = pygame.mixer.Sound("G#2.mp3")
A2sound = pygame.mixer.Sound("A2.mp3")
Asharp2sound = pygame.mixer.Sound("A#2.mp3")
B2sound = pygame.mixer.Sound("B2.mp3")
whiteSounds = [C1sound, D1sound, E1sound, F1sound, G1sound, A1sound, B1sound, C2sound, D2sound, E2sound, F2sound, G2sound, A2sound, B2sound]
blackSounds = [Csharp1sound, Dsharp1sound, None, Fsharp1sound, Gsharp1sound, Asharp1sound, None, Csharp2sound, Dsharp2sound, None, Fsharp2sound, Gsharp2sound, Asharp2sound, None]

activeKeys = []
activeNotes = []
recorded = []
recordedValues = []


keySounds = {
    pygame.K_TAB: C1sound,
    pygame.K_1: Csharp1sound,
    pygame.K_q: D1sound,
    pygame.K_2: Dsharp1sound,
    pygame.K_w: E1sound,
    pygame.K_e: F1sound,
    pygame.K_4: Fsharp1sound,
    pygame.K_r: G1sound,
    pygame.K_5: Gsharp1sound,
    pygame.K_t: A1sound,
    pygame.K_6: Asharp1sound,
    pygame.K_y: B1sound,
    pygame.K_u: C2sound,
    pygame.K_8: Csharp2sound,
    pygame.K_i: D2sound,
    pygame.K_9: Dsharp2sound,
    pygame.K_o: E2sound,
    pygame.K_p: F2sound,
    pygame.K_MINUS: Fsharp2sound,
    pygame.K_LEFTBRACKET: G2sound,
    pygame.K_PLUS: Gsharp2sound,
    pygame.K_RIGHTBRACKET: A2sound,
    pygame.K_BACKSPACE: Asharp2sound,
    pygame.K_BACKSLASH: B2sound,
}
whitekeys = []
blackkeys = []





pygame.init()    
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption('Pygame Piano')
clock = pygame.time.Clock()


def drawKeys():
    whitekeys.clear()
    blackkeys.clear()
    for i in range(0, 14):
        key = pygame.Rect((KEY_WIDTH + SPACE_WIDTH) * i , GAME_HEIGHT - KEY_HEIGHT, KEY_WIDTH, KEY_HEIGHT)
        if key in activeKeys:
            pygame.draw.rect(window, (0, 200, 0), key)  # green when active
        else:
            pygame.draw.rect(window, ("white"), key)  # white when inactive
        whitekeys.append(key)
        key_font = pygame.font.SysFont('Gill Sans', 25)
        key_text = key_font.render(whiteKeyLabels[i], True, 'gray')
        window.blit(key_text, (i * (KEY_WIDTH + SPACE_WIDTH) + KEY_WIDTH/2, KEY_HEIGHT *2))
    for i in chain(range(0, 2), range(3, 6), range(7,9), range(10,13)):
        blackKey = pygame.Rect(3/4*KEY_WIDTH + (KEY_WIDTH + SPACE_WIDTH)*i, GAME_HEIGHT - KEY_HEIGHT, KEY_WIDTH/2, KEY_HEIGHT/2)
        if blackKey in activeKeys:
            pygame.draw.rect(window, (0, 100, 0), blackKey)  # green when active
        else:
            pygame.draw.rect(window, (50, 50, 50), blackKey)  # gray when inactive
        blackkeys.append(blackKey)
        blackKey_font = pygame.font.SysFont('Gill Sans', 24)
        key_text = blackKey_font.render(blackKeyLabels[i], True, 'gray')
        window.blit(key_text, (3/4*KEY_WIDTH + (KEY_WIDTH + SPACE_WIDTH)*i, KEY_HEIGHT+KEY_HEIGHT/2))
def drawNote():
    for x, w, c, h, s, t in activeNotes:
        white_note = pygame.Rect(x, GAME_HEIGHT - KEY_HEIGHT-t, w, h)
        pygame.draw.rect(window, c, white_note)
class RecordNote:
    def __init__(self, note):
        self.startTime = time.time()
        self.endTime = None
        self.finished = False
        self.note = note
        self.duration = 0
    def capTimer(self):
        if not self.finished:
            self.finished = True
            self.endTime = time.time()
            self.duration = self.endTime - self.startTime
    def data(self):
        return self.duration, self.note
class RecordRest:
    def __init__(self):
        self.startTime = time.time()
        self.endTime = None
        self.finished = False
        self.duration = 0
    def capRestTimer(self):
        if not self.finished:
            self.finished = True
            self.endTime = time.time()
            self.duration = self.endTime - self.startTime
    def data(self):
        return self.duration, None
        
    

def drawNoteatX(x, w, c):
    activeNotes.append([x, w, c, 1, False, 0])


while True: # game loop
    growth = 250
    dt = clock.tick(60) / 1000.0
    for note in activeNotes:
        if note[4]:  # shrinking
            note[5] += growth * dt
        else:
            note[3] += growth * dt
            note[5] += growth * dt
    # remove notes that are no longer visible
    activeNotes = [note for note in activeNotes if note[3] > 1]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        isRecording = True
    else:
        isRecording = False
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if click X button on window
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in keySounds:
                keySounds[event.key].play()
                activeKeys.append(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # when pressing a key, start new note growth state as expanding
            # and keep old active notes unchanged
            for i in range(0, 14):
                if whitekeys[i].collidepoint(event.pos):
                    whiteSounds[i].play()
                    activeKeys.append(whitekeys[i])
                    if isRecording:
                        drawNoteatX(whitekeys[i].x, w=KEY_WIDTH, c=(255,0,0))
                    else:
                        drawNoteatX(whitekeys[i].x, w=KEY_WIDTH, c=(0,0,255))
                    for record in recorded:
                        if hasattr(record, "capRestTimer"):
                            record.capRestTimer()
                    if isRecording:
                        recorded.append(RecordNote(whitekeys[i]))
                    

            black_indices = [0,1,3,4,5,7,8,10,11,12]
            for idx in range(len(black_indices)):
                if blackkeys[idx].collidepoint(event.pos):
                    sound = blackSounds[black_indices[idx]]
                    if sound:
                        sound.play()
                    activeKeys.append(blackkeys[idx])
                    drawNoteatX(blackkeys[idx].x, w=KEY_WIDTH/2, c=(0,0,175))
                    for record in recorded:
                        if hasattr(record, "capRestTimer"):
                            record.capRestTimer()
                    if isRecording:
                        recorded.append(RecordNote(blackkeys[idx]))
        if event.type == pygame.MOUSEBUTTONUP:
            for record in recorded:
                if hasattr(record, "capTimer"):
                    record.capTimer()
            if isRecording:
                recorded.append(RecordRest())
            activeKeys.clear()   
            for note in activeNotes:
                note[4] = True
            recordedValues = [r.data() for r in recorded]
            print(recordedValues)
                
            

    window.fill((0, 0, 0))
    drawKeys()
    drawNote()
    pygame.display.update()
    #clock.tick(60)  # Limit the frame rate to 60 FPS