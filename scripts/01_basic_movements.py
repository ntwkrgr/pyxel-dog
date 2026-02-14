"""
Basic Movement Script for Pyxel Dog
Demonstrates basic walking, turning, and sitting movements
"""
from pyxel import Pyxel
pyxel = Pyxel()

# Basic forward movement
print("Walking forward...")
pyxel.Forward(6, 0, 0)
pyxel.Wait(1)  # Wait 1 second

# Turn left
print("Turning left...")
pyxel.Turn(0, 90)  # 0 = left, 90 degrees
pyxel.Wait(1)

# Walk forward again
print("Walking forward...")
pyxel.Forward(4, 0, 0)
pyxel.Wait(1)

# Turn right
print("Turning right...")
pyxel.Turn(1, 90)  # 1 = right, 90 degrees
pyxel.Wait(1)

# Walk backwards
print("Walking backwards...")
pyxel.Backward(4, 0, 0)
pyxel.Wait(1)

# Sit down
print("Sitting down...")
pyxel.Sit()
pyxel.Wait(2)

# Stand up
print("Standing up...")
pyxel.StandUp()
pyxel.Wait(1)

# Shake paw goodbye
print("Shaking paw goodbye!")
pyxel.Shake()
pyxel.Wait(2)

print("Basic movements complete!")
