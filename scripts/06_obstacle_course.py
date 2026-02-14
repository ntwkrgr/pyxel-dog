"""
Obstacle Course Script for Pyxel Dog
Navigate through an imaginary obstacle course
"""
from pyxel import Pyxel
pyxel = Pyxel()

print("🏁 Starting obstacle course!")
pyxel.Lights(7, 0)  # White = ready
pyxel.Wait(1)

# Obstacle 1: Straight path
print("\n1️⃣ Obstacle 1: Straight sprint")
pyxel.Lights(2, 0)  # Green
print("Running forward...")
pyxel.Forward(10, 0, 0)
pyxel.Wait(0.5)
print("✓ Cleared!")

# Obstacle 2: Slalom (zigzag)
print("\n2️⃣ Obstacle 2: Slalom course")
pyxel.Lights(3, 0)  # Yellow
for i in range(3):
    print(f"  Zigzag {i+1}/3")
    pyxel.Turn(0, 30)  # Turn left 30
    pyxel.Forward(3, 0, 0)
    pyxel.Turn(1, 60)  # Turn right 60
    pyxel.Forward(3, 0, 0)
    pyxel.Turn(0, 30)  # Turn left 30 to straighten
    pyxel.Wait(0.3)
print("✓ Cleared!")

# Obstacle 3: The tunnel (crouch and scoot)
print("\n3️⃣ Obstacle 3: Low tunnel")
pyxel.Lights(6, 0)  # Orange
print("Getting low...")
pyxel.Sit()
pyxel.Wait(0.5)
print("Scooting through...")
pyxel.Scoot(6, 0)  # Scoot forward
pyxel.Wait(0.5)
print("Standing up...")
pyxel.StandUp()
pyxel.Wait(0.5)
print("✓ Cleared!")

# Obstacle 4: The spin zone
print("\n4️⃣ Obstacle 4: Spin zone")
pyxel.Lights(5, 0)  # Purple
print("Spinning!")
pyxel.ChaseTail(1)  # Chase tail clockwise
pyxel.Wait(1)
pyxel.ChaseTail(0)  # Chase tail counter-clockwise
pyxel.Wait(1)
print("✓ Cleared!")

# Obstacle 5: The balance beam (slow careful steps)
print("\n5️⃣ Obstacle 5: Balance beam")
pyxel.Lights(6, 0)  # Orange
print("Careful steps...")
for i in range(5):
    pyxel.Forward(2, 0, 0)
    pyxel.Wait(0.6)  # Slow and steady
print("✓ Cleared!")

# Obstacle 6: The jump (simulate with quick movement)
print("\n6️⃣ Obstacle 6: The jump")
pyxel.Lights(1, 0)  # Red
print("Ready...")
pyxel.Wait(0.5)
print("JUMP!")
pyxel.Forward(6, 0, 0)  # Quick burst
pyxel.PlaySound(1, 1, 1)  # Bark
pyxel.Wait(0.3)
print("✓ Cleared!")

# Finish line celebration
print("\n🏆 FINISH LINE!")
pyxel.Lights(2, 0)  # Green

# Victory celebration
print("Victory dance!")
pyxel.Dance()
pyxel.Wait(1)
pyxel.WiggleButt()
pyxel.Wait(1)

# Final celebration sequence
pyxel.PlaySound(5, 1, 1)  # Happy sound
pyxel.Lightshow()
pyxel.Wait(3)

pyxel.Sit()
pyxel.Wait(1)

print("\n🎉 Obstacle course complete! Perfect run!")
print("⭐⭐⭐⭐⭐ 5 Stars!")
