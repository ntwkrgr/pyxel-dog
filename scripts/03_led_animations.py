"""
LED Animation Script for Pyxel Dog
Demonstrates various LED light patterns and animations
"""
from pyxel import Pyxel
import time
import random

pyxel = Pyxel()

print("Starting LED animations...")

# Animation 1: Traffic light
print("Traffic light animation...")
pyxel.led_color(255, 0, 0)  # Red
pyxel.wait(1500)
pyxel.led_color(255, 255, 0)  # Yellow
pyxel.wait(1000)
pyxel.led_color(0, 255, 0)  # Green
pyxel.wait(1500)

# Animation 2: Pulsing effect
print("Pulsing effect...")
for brightness in range(0, 255, 15):
    pyxel.led_color(brightness, 0, brightness)
    pyxel.wait(50)
for brightness in range(255, 0, -15):
    pyxel.led_color(brightness, 0, brightness)
    pyxel.wait(50)

# Animation 3: Color cycle
print("Color cycle...")
for hue in range(0, 360, 20):
    # Simple HSV to RGB conversion for primary colors
    if hue < 60:
        r, g, b = 255, int(hue * 4.25), 0
    elif hue < 120:
        r, g, b = int((120 - hue) * 4.25), 255, 0
    elif hue < 180:
        r, g, b = 0, 255, int((hue - 120) * 4.25)
    elif hue < 240:
        r, g, b = 0, int((240 - hue) * 4.25), 255
    elif hue < 300:
        r, g, b = int((hue - 240) * 4.25), 0, 255
    else:
        r, g, b = 255, 0, int((360 - hue) * 4.25)
    
    pyxel.led_color(r, g, b)
    pyxel.wait(100)

# Animation 4: Strobe effect
print("Strobe effect...")
for i in range(10):
    pyxel.led_color(255, 255, 255)
    pyxel.wait(100)
    pyxel.led_color(0, 0, 0)
    pyxel.wait(100)

# Animation 5: Police lights
print("Police lights...")
for i in range(8):
    pyxel.led_color(255, 0, 0)  # Red
    pyxel.wait(200)
    pyxel.led_color(0, 0, 255)  # Blue
    pyxel.wait(200)

# Animation 6: Firefly effect (random soft glows)
print("Firefly effect...")
for i in range(20):
    r = random.randint(200, 255)
    g = random.randint(150, 200)
    b = random.randint(0, 50)
    pyxel.led_color(r, g, b)
    pyxel.wait(random.randint(100, 300))

# Turn off LEDs
pyxel.led_color(0, 0, 0)
print("LED animations complete!")
