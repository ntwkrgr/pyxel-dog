"""
Dance Party Script for Pyxel Dog
Makes the dog perform a fun dance routine with LED effects
"""
from pyxel import Pyxel
pyxel = Pyxel()

print("🎉 Starting dance party! 🎉")

# Use the built-in dance!
print("Watch me dance!")
pyxel.Dance()
pyxel.Wait(1)

# Wiggle butt excitedly
print("Wiggle wiggle!")
pyxel.WiggleButt()
pyxel.Wait(1)

# Chase tail in a circle
print("Chasing tail...")
pyxel.ChaseTail(1)  # 1 = clockwise
pyxel.Wait(1)

# Another wiggle
pyxel.WiggleButt()
pyxel.Wait(1)

# Wag tail at different speeds
print("Tail wagging...")
pyxel.Wag(1, 1, 3)  # Fast wag
pyxel.Wait(2)

# Shake paw
print("Shake it!")
pyxel.Shake()
pyxel.Wait(2)

# Spin around
print("Spinning...")
for i in range(4):
    pyxel.Turn(1, 90)  # Turn right 90 degrees
    pyxel.Wait(0.3)

# Forward and back shuffle
print("Shuffling...")
for i in range(3):
    pyxel.Forward(2, 0, 0)
    pyxel.Wait(0.2)
    pyxel.Backward(2, 0, 0)
    pyxel.Wait(0.2)

# Finale: Lightshow!
print("Lightshow finale!")
pyxel.Lightshow()
pyxel.Wait(3)

# End with celebration sound and wiggle
pyxel.PlaySound(5, 1, 1)  # Happy sound
pyxel.WiggleButt()
pyxel.Wait(1)

print("Dance party complete! 🎊")
