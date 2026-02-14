"""
Basic Movement Script for Pyxel Dog
Demonstrates basic walking, turning, and sitting movements
"""
from pyxel import Pyxel
pyxel = Pyxel()

# Basic forward movement
print("Walking forward...")
pyxel.walk_forward(steps=5)
pyxel.wait(1000)  # Wait 1 second

# Turn left
print("Turning left...")
pyxel.turn_left(degrees=90)
pyxel.wait(1000)

# Walk forward again
print("Walking forward...")
pyxel.walk_forward(steps=3)
pyxel.wait(1000)

# Turn right
print("Turning right...")
pyxel.turn_right(degrees=90)
pyxel.wait(1000)

# Walk backwards
print("Walking backwards...")
pyxel.walk_backward(steps=3)
pyxel.wait(1000)

# Sit down
print("Sitting down...")
pyxel.sit()
pyxel.wait(2000)

# Stand up
print("Standing up...")
pyxel.stand()
pyxel.wait(1000)

# Wave goodbye
print("Waving goodbye!")
pyxel.wave()
pyxel.wait(1000)

print("Basic movements complete!")
