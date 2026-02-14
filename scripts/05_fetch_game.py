"""
Fetch Game Script for Pyxel Dog
Simulates a fetch game with the dog
"""
from pyxel import Pyxel
import random

pyxel = Pyxel()

print("🎾 Let's play fetch!")

def excited_wiggle():
    """Show excitement by wiggling"""
    for i in range(3):
        pyxel.turn_left(degrees=20)
        pyxel.wait(200)
        pyxel.turn_right(degrees=40)
        pyxel.wait(200)
        pyxel.turn_left(degrees=20)
        pyxel.wait(200)

def run_to_ball():
    """Run to fetch the ball"""
    print("Running to get the ball...")
    pyxel.led_color(255, 255, 0)  # Yellow = focused
    
    # Random distance
    steps = random.randint(5, 10)
    pyxel.walk_forward(steps=steps)
    pyxel.wait(500)

def bring_back():
    """Bring the ball back"""
    print("Bringing it back!")
    pyxel.led_color(0, 255, 0)  # Green = success
    
    # Turn around
    pyxel.turn_left(degrees=180)
    pyxel.wait(500)
    
    # Come back
    pyxel.walk_forward(steps=5)
    pyxel.wait(500)

def celebrate():
    """Celebrate successful fetch"""
    print("Good dog! 🎉")
    pyxel.play_sound("happy")
    pyxel.led_color(255, 0, 255)  # Purple = celebration
    
    # Happy dance
    for i in range(3):
        pyxel.wave()
        pyxel.wait(300)
    
    excited_wiggle()

# Game loop
rounds = 3

for round_num in range(1, rounds + 1):
    print(f"\n--- Round {round_num}/{rounds} ---")
    
    # Get ready
    print("Get ready...")
    excited_wiggle()
    pyxel.led_color(255, 165, 0)  # Orange = ready
    pyxel.wait(1000)
    
    # "Throw" the ball (simulate with random direction)
    print("🎾 Ball thrown!")
    direction = random.choice(["left", "right", "straight"])
    
    if direction == "left":
        pyxel.turn_left(degrees=45)
    elif direction == "right":
        pyxel.turn_right(degrees=45)
    
    pyxel.wait(500)
    
    # Fetch!
    run_to_ball()
    pyxel.wait(1000)
    
    # Bring back
    bring_back()
    
    # Celebrate
    celebrate()
    
    # Rest between rounds
    if round_num < rounds:
        print("Resting for next round...")
        pyxel.sit()
        pyxel.led_color(0, 0, 255)  # Blue = resting
        pyxel.wait(2000)
        pyxel.stand()

# End game
print("\n🏆 Fetch game complete! Great job!")
pyxel.sit()
pyxel.play_sound("happy")
pyxel.led_color(0, 255, 0)
pyxel.wait(2000)
