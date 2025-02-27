# Asteroids Clone (Pygame)
A classic **Asteroids** remake built using **Pygame** and object-oriented programming principles. This project was part of a guided course and helped reinforce skills in game loops, user input handling, collision detection, and object management.

## Gameplay Features

#### Ship Controls

* **Left Arrow:** Rotate left
* **Right Arrow:** Rotate right
* **Up Arrow:** Move forward
* **Down Arrow:** Move backward

#### Bullets

* Small circles that move in a straight line at a constant speed
* Spawned by pressing **spacebar**
* Destroy asteroids on impact, causing them to split (if applicable)

#### Asteroid Mechanics

* Large asteroids split into **two medium asteroids**
* Medium asteroids split into **two small asteroids**
* Small asteroids disappear upon destruction

#### Collision Detection

* Implemented using **circle-based collision detection**
* If the distance between two object centers is less than the sum of their radii, a collision occurs

## Installation & Running the Game

### Requirements
* Python 3.x
* Pygame (`pip install pygame`)

### Clone the Repository
To download the game, open a terminal and run:
```bash
git clone https://github.com/MittenzDev/asteroids.git
cd asteroids
```

### Run the Game
```bash
python asteroids.py
```
