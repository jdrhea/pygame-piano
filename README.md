# Pygame Piano

A small interactive piano built with Pygame. Use your computer keyboard or the mouse to play notes; the app shows visual feedback and includes a simple, experimental recording mode.

**Features**
- Play notes via keyboard or mouse clicks.
- Visual key highlighting and animated note bars.
- Experimental recording/timing while holding the Space key.

**Requirements**
- Python 3.8+
- `pygame` (install with `pip install pygame`)
- A set of note audio files (MP3) placed beside [pypiano.py](pypiano.py):
	- C1.mp3, C#1.mp3, D1.mp3, D#1.mp3, E1.mp3, F1.mp3, F#1.mp3, G1.mp3, G#1.mp3, A1.mp3, A#1.mp3, B1.mp3,
	- C2.mp3, C#2.mp3, D2.mp3, D#2.mp3, E2.mp3, F2.mp3, F#2.mp3, G2.mp3, G#2.mp3, A2.mp3, A#2.mp3, B2.mp3

**Install**

```bash
python3 -m pip install --user pygame
```

**Run**

```bash
python3 pypiano.py
```

**Controls (keyboard → note)**
- `Tab` : C1
- `1` : C#1
- `q` : D1
- `2` : D#1
- `w` : E1
- `e` : F1
- `4` : F#1
- `r` : G1
- `5` : G#1
- `t` : A1
- `6` : A#1
- `y` : B1
- `u` : C2
- `8` : C#2
- `i` : D2
- `9` : D#2
- `o` : E2
- `p` : F2
- `-` : F#2
- `[` : G2
- `+` : G#2
- `]` : A2
- `Backspace` : A#2
- `\\` : B2

Mouse:
- Click a white or black key to play the corresponding note and spawn an animated note bar.

Recording (experimental):
- Hold `Space` while clicking/playing to enable basic timing/recording behavior. This feature is partially implemented and may be unstable.

**Implementation notes**
- The main script is [pypiano.py](pypiano.py). It draws keys, maps keyboard input to sounds, and animates notes.
- Sounds are loaded via `pygame.mixer.Sound("<NOTE>.mp3")` so audio files must be named exactly as listed and placed in the same folder.

**Contributing**
- Issues and pull requests welcome. If you add features (MIDI input, better recording/export, piano scaling), include short instructions and update this README.

**License**
- See [LICENSE](LICENSE).
