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
    pyxel.WiggleButt()
    pyxel.Wag(1, 1, 3)  # Fast tail wag
    pyxel.Wait(1)

def run_to_ball():
    """Run to fetch the ball"""
    print("Running to get the ball...")
    pyxel.Lights(3, 0)  # Yellow = focused
    
    # Random distance
    distance = random.randint(6, 12)
    pyxel.Forward(distance, 0, 0)
    pyxel.Wait(0.5)

def bring_back():
    """Bring the ball back"""
    print("Bringing it back!")
    pyxel.Lights(2, 0)  # Green = success
    
    # Turn around
    pyxel.Turn(0, 180)  # Turn left 180 degrees
    pyxel.Wait(0.5)
    
    # Come back
    pyxel.Forward(8, 0, 0)
    pyxel.Wait(0.5)

def celebrate():
    """Celebrate successful fetch"""
    print("Good dog! 🎉")
    pyxel.PlaySound(5, 1, 1)  # Happy sound
    pyxel.Lights(5, 0)  # Celebration color
    
    # Happy dance
    pyxel.Shake()
    pyxel.Wait(2)
    
    excited_wiggle()

# Game loop
rounds = 3

for round_num in range(1, rounds + 1):
    print(f"\n--- Round {round_num}/{rounds} ---")
    
    # Get ready
    print("Get ready...")
    excited_wiggle()
    pyxel.Lights(6, 0)  # Orange = ready
    pyxel.Wait(1)
    
    # "Throw" the ball (simulate with random direction)
    print("🎾 Ball thrown!")
    direction = random.choice(["left", "right", "straight"])
    
    if direction == "left":
        pyxel.Turn(0, 45)  # Turn left 45 degrees
    elif direction == "right":
        pyxel.Turn(1, 45)  # Turn right 45 degrees
    
    pyxel.Wait(0.5)
    
    # Fetch!
    run_to_ball()
    pyxel.Wait(1)
    
    # Bring back
    bring_back()
    
    # Celebrate
    celebrate()
    
    # Rest between rounds
    if round_num < rounds:
        print("Resting for next round...")
        pyxel.Sit()
        pyxel.Lights(4, 0)  # Blue = resting
        pyxel.Wait(2)
        pyxel.StandUp()

# End game
print("\n🏆 Fetch game complete! Great job!")
pyxel.Sit()
pyxel.PlaySound(5, 1, 1)  # Happy sound
pyxel.Lights(2, 0)  # Green
pyxel.Wait(2)
