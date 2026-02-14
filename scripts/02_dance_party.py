"""
Dance Party Script for Pyxel Dog
Makes the dog perform a fun dance routine with LED effects
"""
from pyxel import Pyxel
pyxel = Pyxel()

print("🎉 Starting dance party! 🎉")

# Start with some exciting LED colors
pyxel.led_color(255, 0, 0)  # Red
pyxel.wait(200)

# Dance move 1: Spin around
print("Spinning...")
for i in range(4):
    pyxel.turn_left(degrees=90)
    pyxel.led_color(255, 0, 255)  # Purple
    pyxel.wait(300)

# Dance move 2: Forward and back shuffle
print("Shuffling...")
for i in range(3):
    pyxel.walk_forward(steps=1)
    pyxel.led_color(0, 255, 0)  # Green
    pyxel.wait(200)
    pyxel.walk_backward(steps=1)
    pyxel.led_color(0, 0, 255)  # Blue
    pyxel.wait(200)

# Dance move 3: The wave
print("Waving...")
for i in range(5):
    pyxel.wave()
    pyxel.led_color(255, 255, 0)  # Yellow
    pyxel.wait(300)

# Dance move 4: Turn and sit
print("Turn and sit...")
pyxel.turn_right(degrees=180)
pyxel.led_color(255, 128, 0)  # Orange
pyxel.wait(500)
pyxel.sit()
pyxel.wait(500)
pyxel.stand()

# Finale: Rainbow LED effect
print("Rainbow finale!")
colors = [
    (255, 0, 0),    # Red
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (75, 0, 130),   # Indigo
    (148, 0, 211)   # Violet
]

for color in colors:
    pyxel.led_color(*color)
    pyxel.turn_left(degrees=51)  # Spin while showing rainbow
    pyxel.wait(200)

# End with celebration
pyxel.play_sound("happy")
pyxel.led_color(255, 255, 255)  # White
pyxel.wait(1000)

print("Dance party complete! 🎊")
