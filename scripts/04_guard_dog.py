"""
Guard Dog Script for Pyxel Dog
Makes the dog patrol an area and respond to sensors
"""
from pyxel import Pyxel
pyxel = Pyxel()

print("🐕 Guard dog mode activated!")
print("Patrolling the perimeter...")

# Set alert LED color
pyxel.led_color(0, 255, 0)  # Green = all clear

# Patrol pattern
def patrol():
    """Patrol in a square pattern"""
    for i in range(4):
        print(f"Patrol leg {i+1}/4")
        pyxel.walk_forward(steps=5)
        pyxel.wait(500)
        
        # Check sensors
        if pyxel.get_distance() < 20:  # If something is close
            alert()
            return False
        
        pyxel.turn_right(degrees=90)
        pyxel.wait(500)
    
    return True

def alert():
    """Alert behavior when something is detected"""
    print("⚠️ ALERT! Something detected!")
    
    # Flash red lights
    for i in range(5):
        pyxel.led_color(255, 0, 0)
        pyxel.wait(200)
        pyxel.led_color(0, 0, 0)
        pyxel.wait(200)
    
    # Bark
    pyxel.play_sound("bark")
    pyxel.wait(500)
    
    # Defensive stance
    print("Taking defensive stance...")
    pyxel.sit()
    pyxel.wait(1000)
    
    # More barking
    for i in range(3):
        pyxel.play_sound("bark")
        pyxel.led_color(255, 0, 0)
        pyxel.wait(500)

# Run patrol
patrol_count = 0
max_patrols = 3

while patrol_count < max_patrols:
    print(f"\nStarting patrol {patrol_count + 1}/{max_patrols}")
    
    if not patrol():
        # Alert was triggered
        break
    
    patrol_count += 1
    
    if patrol_count < max_patrols:
        print("Patrol complete. Resting briefly...")
        pyxel.sit()
        pyxel.wait(2000)
        pyxel.stand()
        pyxel.wait(500)

# End patrol
print("\n✅ Guard duty complete!")
pyxel.led_color(0, 0, 255)  # Blue = off duty
pyxel.sit()
pyxel.wait(1000)
