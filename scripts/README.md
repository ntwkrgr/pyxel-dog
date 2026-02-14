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
**Demonstrates:** Walking, turning, sitting, standing, and waving

A beginner-friendly script that shows the fundamental movement commands. Perfect for learning the basics of Pyxel dog control.

**Features:**
- Forward and backward walking
- Left and right turns
- Sitting and standing
- Waving gesture

**Run time:** ~10 seconds

---

### 2. Dance Party (`02_dance_party.py`)
**Demonstrates:** Complex movement sequences with LED synchronization

Make your Pyxel dog dance with a choreographed routine featuring spinning, shuffling, waving, and a rainbow LED finale!

**Features:**
- 360° spins
- Forward/backward shuffle
- Wave moves
- Rainbow LED color cycling
- Sound effects

**Run time:** ~20 seconds

---

### 3. LED Animations (`03_led_animations.py`)
**Demonstrates:** Various LED light patterns and color effects

A showcase of different LED animation techniques including color cycles, pulsing effects, and strobe patterns.

**Features:**
- Traffic light sequence
- Pulsing brightness effect
- Full color spectrum cycle
- Strobe effect
- Police lights
- Firefly random glow effect

**Run time:** ~30 seconds

---

### 4. Guard Dog (`04_guard_dog.py`)
**Demonstrates:** Sensor-based reactive behavior and patrol patterns

Turn your Pyxel dog into a security guard that patrols an area and responds to detected objects.

**Features:**
- Square patrol pattern
- Distance sensor monitoring
- Alert behavior with barking
- LED status indicators (green=clear, red=alert)
- Defensive stance

**Run time:** Variable (depends on sensor input)

---

### 5. Fetch Game (`05_fetch_game.py`)
**Demonstrates:** Game-like interactive behavior with randomization

Play an automated fetch game where the dog chases after an imaginary ball in random directions.

**Features:**
- Excited wiggle behavior
- Random direction selection
- Running and retrieving
- Victory celebration
- Multi-round game play (3 rounds)

**Run time:** ~40 seconds

---

### 6. Obstacle Course (`06_obstacle_course.py`)
**Demonstrates:** Complex navigation and sequential behaviors

Watch your Pyxel dog navigate through a challenging obstacle course with 6 different obstacles.

**Features:**
- Straight sprint
- Slalom zigzag
- Low tunnel crawl
- Spin zone
- Balance beam (careful steps)
- Jump obstacle
- Victory celebration

**Run time:** ~45 seconds

---

## Common API Commands Used

### Movement
- `pyxel.walk_forward(steps=n)` - Walk forward n steps
- `pyxel.walk_backward(steps=n)` - Walk backward n steps
- `pyxel.turn_left(degrees=n)` - Turn left n degrees
- `pyxel.turn_right(degrees=n)` - Turn right n degrees

### Postures
- `pyxel.sit()` - Sit down
- `pyxel.stand()` - Stand up
- `pyxel.wave()` - Wave paw

### LED Control
- `pyxel.led_color(r, g, b)` - Set LED color (0-255 for each channel)

### Sounds
- `pyxel.play_sound("sound_name")` - Play a sound effect
  - Common sounds: "bark", "happy"

### Sensors
- `pyxel.get_distance()` - Get distance sensor reading

### Timing
- `pyxel.wait(milliseconds)` - Wait for specified milliseconds

---

## Tips for Creating Your Own Scripts

1. **Start Simple:** Begin with basic movements and gradually add complexity
2. **Use Timing:** Add `pyxel.wait()` calls to let movements complete before starting new ones
3. **Combine LEDs and Movement:** Sync LED colors with actions for visual feedback
4. **Add Personality:** Use random variations and sound effects to make behaviors more interesting
5. **Test Incrementally:** Run short sequences to ensure they work before building longer scripts

## Customization Ideas

- **Music Sync:** Create dance routines synchronized to your favorite songs
- **Maze Solver:** Use sensors to navigate through a maze
- **Follow Me:** Make the dog follow objects using distance sensors
- **Light Show:** Create elaborate LED patterns and sequences
- **Trick Training:** Combine movements into unique tricks
- **Battle Bot:** Create defensive and offensive behaviors

## Safety Notes

- Ensure your Pyxel dog has enough space to move safely
- Keep the dog away from stairs and edges when running automated scripts
- Monitor the dog during script execution
- Be ready to stop scripts if needed

## Contributing

Feel free to create your own scripts and share them! The more creative behaviors we can create for Pyxel dog, the better.

---

**Happy coding with your Pyxel dog! 🐕🎉**
