"""
Obstacle Course Script for Pyxel Dog
Navigate through an imaginary obstacle course
"""
from pyxel import Pyxel
pyxel = Pyxel()

print("🏁 Starting obstacle course!")
pyxel.led_color(255, 255, 255)  # White = ready
pyxel.wait(1000)

# Obstacle 1: Straight path
print("\n1️⃣ Obstacle 1: Straight sprint")
pyxel.led_color(0, 255, 0)
print("Running forward...")
pyxel.walk_forward(steps=8)
pyxel.wait(500)
print("✓ Cleared!")

# Obstacle 2: Slalom (zigzag)
print("\n2️⃣ Obstacle 2: Slalom course")
pyxel.led_color(255, 255, 0)
for i in range(3):
    print(f"  Zigzag {i+1}/3")
    pyxel.turn_left(degrees=30)
    pyxel.walk_forward(steps=2)
    pyxel.turn_right(degrees=60)
    pyxel.walk_forward(steps=2)
    pyxel.turn_left(degrees=30)
    pyxel.wait(300)
print("✓ Cleared!")

# Obstacle 3: The tunnel (crouch and walk)
print("\n3️⃣ Obstacle 3: Low tunnel")
pyxel.led_color(0, 255, 255)
print("Getting low...")
pyxel.sit()
pyxel.wait(500)
print("Crawling through...")
for i in range(4):
    pyxel.walk_forward(steps=1)
    pyxel.wait(400)
print("Standing up...")
pyxel.stand()
pyxel.wait(500)
print("✓ Cleared!")

# Obstacle 4: The spin zone
print("\n4️⃣ Obstacle 4: Spin zone")
pyxel.led_color(255, 0, 255)
print("Spinning!")
for i in range(2):
    pyxel.turn_right(degrees=360)
    pyxel.wait(300)
print("✓ Cleared!")

# Obstacle 5: The balance beam (slow careful steps)
print("\n5️⃣ Obstacle 5: Balance beam")
pyxel.led_color(255, 128, 0)
print("Careful steps...")
for i in range(5):
    pyxel.walk_forward(steps=1)
    pyxel.wait(600)  # Slow and steady
print("✓ Cleared!")

# Obstacle 6: The jump (simulate with quick movement)
print("\n6️⃣ Obstacle 6: The jump")
pyxel.led_color(255, 0, 0)
print("Ready...")
pyxel.wait(500)
print("JUMP!")
pyxel.walk_forward(steps=3)  # Quick burst
pyxel.play_sound("bark")
pyxel.wait(300)
print("✓ Cleared!")

# Finish line celebration
print("\n🏆 FINISH LINE!")
pyxel.led_color(0, 255, 0)

# Victory celebration
print("Victory dance!")
for i in range(4):
    pyxel.turn_left(degrees=90)
    pyxel.wave()
    pyxel.wait(300)

# Final celebration sequence
pyxel.play_sound("happy")
for i in range(5):
    if i % 2 == 0:
        pyxel.led_color(255, 215, 0)  # Gold
    else:
        pyxel.led_color(255, 255, 255)  # White
    pyxel.wait(300)

pyxel.sit()
pyxel.wait(1000)

print("\n🎉 Obstacle course complete! Perfect run!")
print("⭐⭐⭐⭐⭐ 5 Stars!")
