"""
LED Animation Script for Pyxel Dog
Demonstrates various LED light patterns and animations
"""
from pyxel import Pyxel
pyxel = Pyxel()

print("Starting LED animations...")

# Animation 1: Built-in lightshow
print("Rainbow lightshow...")
pyxel.Lightshow()
pyxel.Wait(3)

# Animation 2: Traffic light sequence
print("Traffic light animation...")
pyxel.Lights(1, 1)  # Red on head
pyxel.Wait(1.5)
pyxel.Lights(3, 1)  # Yellow on head
pyxel.Wait(1)
pyxel.Lights(2, 1)  # Green on head
pyxel.Wait(1.5)

# Animation 3: Different body parts
print("Lighting up different parts...")
pyxel.Lights(4, 1)  # Blue on head
pyxel.Wait(0.5)
pyxel.Lights(4, 2)  # Blue on body
pyxel.Wait(0.5)
pyxel.Lights(4, 3)  # Blue on tail
pyxel.Wait(0.5)

# Animation 4: Color sequence on all parts
print("Full body color sequence...")
colors = [1, 2, 3, 4, 5, 6]  # Various colors
for color in colors:
    pyxel.Lights(color, 0)  # 0 = all parts
    pyxel.Wait(0.5)

# Animation 5: Alternating lights
print("Alternating pattern...")
for i in range(6):
    pyxel.Lights(1, 1)  # Red head
    pyxel.Wait(0.3)
    pyxel.Lights(4, 1)  # Blue head
    pyxel.Wait(0.3)

# Animation 6: Body wave
print("Body wave effect...")
for i in range(3):
    pyxel.Lights(5, 1)  # Color on head
    pyxel.Wait(0.2)
    pyxel.Lights(5, 2)  # Color on body
    pyxel.Wait(0.2)
    pyxel.Lights(5, 3)  # Color on tail
    pyxel.Wait(0.2)

# Finale: Another lightshow
print("Grand finale lightshow!")
pyxel.Lightshow()
pyxel.Wait(3)

# Turn off LEDs
pyxel.Lights(0, 0)  # Off
print("LED animations complete!")
