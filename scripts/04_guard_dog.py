"""
Guard Dog Script for Pyxel Dog
Makes the dog patrol an area and respond to sensors
"""
from pyxel import Pyxel
pyxel = Pyxel()

print("🐕 Guard dog mode activated!")
print("Patrolling the perimeter...")

# Set alert LED color - green = all clear
pyxel.Lights(2, 0)  # Green on all parts
pyxel.Wait(1)

# Enable proximity detection
pyxel.SetProximity(1)  # Turn on proximity sensor

# Patrol pattern
def patrol():
    """Patrol in a square pattern"""
    for i in range(4):
        print(f"Patrol leg {i+1}/4")
        pyxel.Forward(6, 0, 0)
        pyxel.Wait(0.5)
        
        # Check sensors
        if pyxel.Proximity(1):  # If something is detected
            alert()
            return False
        
        pyxel.Turn(1, 90)  # Turn right 90 degrees
        pyxel.Wait(0.5)
    
    return True

def alert():
    """Alert behavior when something is detected"""
    print("⚠️ ALERT! Something detected!")
    
    # Flash red lights
    for i in range(5):
        pyxel.Lights(1, 0)  # Red on all parts
        pyxel.Wait(0.2)
        pyxel.Lights(0, 0)  # Off
        pyxel.Wait(0.2)
    
    # Bark
    pyxel.PlaySound(1, 1, 1)  # Bark sound
    pyxel.Wait(0.5)
    
    # Defensive stance
    print("Taking defensive stance...")
    pyxel.Sit()
    pyxel.Wait(1)
    
    # More barking with red lights
    for i in range(3):
        pyxel.PlaySound(1, 1, 1)  # Bark
        pyxel.Lights(1, 0)  # Red
        pyxel.Wait(0.5)

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
        pyxel.Sit()
        pyxel.Wait(2)
        pyxel.StandUp()
        pyxel.Wait(0.5)

# End patrol
print("\n✅ Guard duty complete!")
pyxel.Lights(4, 0)  # Blue = off duty
pyxel.Sit()
pyxel.Wait(1)
