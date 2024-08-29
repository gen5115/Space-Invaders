# Space Invaders Game

## Description

Welcome to my Space Invaders game! This is a classic arcade-style game where you control a spaceship to shoot at descending aliens. The goal is to destroy all the enemies before they reach the bottom of the screen.

## Features

- **Player Controls:** Move the spaceship left and right using arrow keys and shoot bullets with the space bar.
- **Enemies:** Aliens move horizontally and drop down when they hit the edge of the screen.
- **Scoring:** Earn points by hitting enemies with bullets.
- **Game Over:** The game ends when an enemy reaches the player's position. You can restart by pressing 'R'.

## How It Works

1. **Player Movement:** Use arrow keys to move the spaceship.
2. **Shooting:** Press the space bar to fire bullets.
3. **Enemy Movement:** Enemies move left and right and drop down when hitting the screen edge.
4. **Collision Detection:** When a bullet hits an enemy, the enemy is destroyed, and the score is updated.
5. **Game Over:** If an enemy reaches the player's position, the game ends and displays a game over screen. Press 'R' to restart.

## Installation

To run this game on your local machine, follow these steps:

1. **Clone the Repository:**
   git clone https://github.com/gen5115/Space-Invaders.git
   
 2.**Navigate to the Project Directory:**
   cd Space-Invaders
   
3. **Install Dependencies:**
  Make sure you have Python and Pygame installed. You can install Pygame using pip:
pip install pygame

 4. **Run the Game:**
     space_invaders.py

    
## Challenges and Solutions

1. **Collision Detection:**

Challenge: Ensuring accurate collision detection between bullets and enemies.
Solution: Used distance calculations to determine collisions.

2. **Enemy Movement:**

Challenge: Smooth movement and boundary handling.
Solution: Implemented horizontal movement with boundary checks.

3.**Game Over Handling:**

Challenge: Managing the game over screen and restart functionality.
Solution: Added a game over screen and a restart option using a loop to wait for user input.

## Key Learnings
- **Game Development:** Gained experience in game mechanics and using Pygame for development.
- **Problem-Solving:** Developed skills in debugging and resolving issues related to game logic and collision detection.

## Links
https://youtu.be/FfWpgLFMI7w?si=VQ9Mx-mdCJJH2J2W - This video guided the development of the game.
GitHub Repository
