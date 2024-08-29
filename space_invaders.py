import pygame
import random
import math
from pygame import mixer

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Caption and Icon
pygame.display.set_caption("Python Space Invaders")
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

# Background
bg = pygame.image.load('images/bg.jpg')
bg = pygame.transform.scale(bg, (screen_width, screen_height))  # Fit to screen

# Background Music
mixer.music.load("audios/background.wav")
mixer.music.play(-1)  # -1 for loop

# Player
player_img = pygame.image.load('images/player.png')
playerX = 350
playerY = 480
playerX_change = 0

# Enemy
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 7

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('images/enemy.png'))
    enemyX.append(random.randint(0, 760))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(20)

# Bullet
bullet_img = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

testX = 10
testY = 10

gameOver = pygame.font.Font("freesansbold.ttf", 64)  # Game over Font

# Start Menu Font
start_font = pygame.font.Font("freesansbold.ttf", 56)  # Start Menu

# Start Menu Function
def start_menu():
    waiting = True
    while waiting:
        screen.fill((0, 0, 0))
        start_text = start_font.render("Press Enter to Start", True, (255, 255, 255))
        screen.blit(start_text, (190, 250))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

# Displaying score function
def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# GAME Over function
def game_over_text():
    over_text = gameOver.render("GAME OVER", True, (255, 255, 255))
    restart_text = font.render("Press R to Restart", True, (255, 255, 255))  # Text to instruct restart
    screen.blit(over_text, (200, 250))
    screen.blit(restart_text, (230, 320))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False  # Exit the loop and restart the game

    restart_game()

                   
# Restart Game function
def restart_game():
    global playerX, playerY, playerX_change, bulletX, bulletY, bullet_state, score_value
    playerX = 350
    playerY = 480
    playerX_change = 0
    bulletX = 0
    bulletY = 480
    bullet_state = "ready"
    score_value = 0

    for i in range(num_of_enemies):
        enemyX[i] = random.randint(0, 760)
        enemyY[i] = random.randint(50, 150)

    game_loop()

# Player function
def player(x, y):
    screen.blit(player_img, (x, y))

# Enemy function
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

# Bullet function
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))  # Added values so bullet stays in center 

# Collision function
def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    return distance < 27

# Game Loop
def game_loop():
    global running, playerX, playerY, playerX_change, bulletX, bulletY, bullet_state, score_value
    game_active = False
    running = True
    start_menu()  

    while running:

        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))  # Background Image

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Keydown events for player movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -0.8
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0.8

                # Bullet firing
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound("audios/laser.wav")
                        bullet_sound.play()
                        bulletX = playerX  # Current X coordinate of spaceship
                        fire_bullet(bulletX, bulletY)

            # Keyup events to stop player movement
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Added Boundaries
        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy movement and collision detection
        for i in range(num_of_enemies):
            # GAME OVER text
            if enemyY[i] >= playerY - 80:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]

            if enemyX[i] <= 0:
                enemyX_change[i] = 1.5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -1.5
                enemyY[i] += enemyY_change[i]

            # Collision Function
            collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                collision_sound = mixer.Sound("audios/explosion.wav")
                collision_sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 760)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        # Bullet movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        # Function calls
        player(playerX, playerY)
        show_score(testX, testY)

        # Display update
        pygame.display.update()

game_loop()
