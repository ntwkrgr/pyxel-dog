# Pyxel Dog Python Scripts 🐕

This collection contains fun and interactive Python scripts for the Pyxel robot dog toy. Each script demonstrates different behaviors and capabilities of the Pyxel dog.

## Getting Started

All scripts start with the standard Pyxel initialization:

```python
from pyxel import Pyxel
pyxel = Pyxel()
```

## Available Scripts

### 1. Basic Movements (`01_basic_movements.py`)
**Demonstrates:** Walking, turning, sitting, standing, and shaking

A beginner-friendly script that shows the fundamental movement commands. Perfect for learning the basics of Pyxel dog control.

**Features:**
- Forward and backward walking
- Left and right turns
- Sitting and standing
- Shake paw gesture

**Run time:** ~10 seconds

---

### 2. Dance Party (`02_dance_party.py`)
**Demonstrates:** Built-in dance moves, wiggle butt, tail chasing, and lightshow

Make your Pyxel dog dance with choreographed routines featuring the built-in Dance command, tail wags, spins, and a spectacular lightshow finale!

**Features:**
- Built-in Dance() command
- WiggleButt() excitement
- ChaseTail() in circles
- Tail wagging at various speeds
- Lightshow() rainbow finale

**Run time:** ~20 seconds

---

### 3. LED Animations (`03_led_animations.py`)
**Demonstrates:** Various LED light patterns using the Lights command

A showcase of different LED animation techniques including the rainbow Lightshow and custom color patterns on different body parts.

**Features:**
- Rainbow Lightshow()
- Traffic light sequence
- Body part specific lighting (head, body, tail)
- Full body color sequences
- Alternating patterns
- Body wave effect

**Run time:** ~20 seconds

---

### 4. Guard Dog (`04_guard_dog.py`)
**Demonstrates:** Sensor-based reactive behavior and patrol patterns

Turn your Pyxel dog into a security guard that patrols an area using the Proximity sensor to detect objects.

**Features:**
- Square patrol pattern
- Proximity sensor monitoring
- Alert behavior with barking
- LED status indicators (green=clear, red=alert, blue=off duty)
- Defensive stance

**Run time:** Variable (depends on sensor input)

---

### 5. Fetch Game (`05_fetch_game.py`)
**Demonstrates:** Game-like interactive behavior with randomization

Play an automated fetch game where the dog chases after an imaginary ball in random directions.

**Features:**
- WiggleButt() excitement
- Random direction selection
- Running and retrieving
- Victory celebration with Shake()
- Multi-round game play (3 rounds)

**Run time:** ~40 seconds

---

### 6. Obstacle Course (`06_obstacle_course.py`)
**Demonstrates:** Complex navigation and sequential behaviors

Watch your Pyxel dog navigate through a challenging obstacle course with 6 different obstacles.

**Features:**
- Straight sprint
- Slalom zigzag
- Low tunnel with Scoot()
- Spin zone with ChaseTail()
- Balance beam (careful steps)
- Jump obstacle
- Victory celebration with Dance() and Lightshow()

**Run time:** ~45 seconds

---

## Common API Commands Used

### Movement
- `pyxel.Forward(distance, 0, 0)` - Walk forward (distance in units)
- `pyxel.Backward(distance, 0, 0)` - Walk backward (distance in units)
- `pyxel.Turn(direction, degrees)` - Turn (0=left, 1=right)
- `pyxel.Scoot(distance, 0)` - Scoot while sitting

### Postures & Actions
- `pyxel.Sit()` - Sit down
- `pyxel.StandUp()` - Stand up
- `pyxel.Shake()` - Shake paw
- `pyxel.Dance()` - Perform built-in dance
- `pyxel.WiggleButt()` - Wiggle excitedly
- `pyxel.ChaseTail(direction)` - Chase tail (0 or 1)
- `pyxel.Wag(param1, param2, speed)` - Wag tail
- `pyxel.Pee()` - Raise leg with sound

### LED Control
- `pyxel.Lights(color, location)` - Set LED color and location
  - Colors: 0=off, 1=red, 2=green, 3=yellow, 4=blue, 5=purple, 6=orange, 7=white
  - Locations: 0=all, 1=head, 2=body, 3=tail
- `pyxel.Lightshow()` - Rainbow light show

### Sounds
- `pyxel.PlaySound(sound, volume, speed)` - Play a sound effect
  - Sound 1: Bark
  - Sound 5: Happy sound
  - More sounds available (see API docs)

### Sensors
- `pyxel.Proximity(count)` - Detect proximity triggers
- `pyxel.SetProximity(on_off)` - Enable/disable proximity sensor (1=on, 0=off)
- `pyxel.Touch(count)` - Detect head touches
- `pyxel.Listen(count)` - Detect claps

### Facial Expressions
- `pyxel.Eyes(left_emotion, right_emotion)` - Set eye emotions
- `pyxel.Mouth(emotion)` - Set mouth emotion

### Timing & Control
- `pyxel.Wait(seconds)` - Wait for specified seconds
- `pyxel.SetBlocking(0 or 1)` - Set command blocking mode

### Special Commands
- `pyxel.Treat()` - Activate proximity twice for surprise
- `pyxel.PlaySound(788, 1, 1)` - Secret sounds (codes TBA)

---

## Tips for Creating Your Own Scripts

1. **Start Simple:** Begin with basic movements and gradually add complexity
2. **Use Timing:** Add `pyxel.Wait()` calls to let movements complete before starting new ones
3. **Combine Commands:** Mix movements with Lights() and PlaySound() for engaging behaviors
4. **Use Built-ins:** Take advantage of Dance(), WiggleButt(), and Lightshow() for impressive effects
5. **Sensor Interaction:** Use Proximity(), Touch(), and Listen() for interactive behaviors
6. **Test Incrementally:** Run short sequences to ensure they work before building longer scripts

## Customization Ideas

- **Music Sync:** Create dance routines synchronized to your favorite songs
- **Maze Solver:** Use Proximity sensor to navigate through a maze
- **Follow Me:** Make the dog follow objects using Proximity sensor
- **Light Show:** Create elaborate LED patterns and sequences using Lights()
- **Trick Training:** Combine movements into unique tricks
- **Interactive Games:** Use Touch() and Listen() for interactive play

## Safety Notes

- Ensure your Pyxel dog has enough space to move safely
- Keep the dog away from stairs and edges when running automated scripts
- Monitor the dog during script execution
- Be ready to stop scripts if needed

## Contributing

Feel free to create your own scripts and share them! The more creative behaviors we can create for Pyxel dog, the better.

---

**Happy coding with your Pyxel dog! 🐕🎉**
