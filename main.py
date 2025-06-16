import pygame
import random
import math

from pygame import mixer

pygame.init()

# title
pygame.display.set_caption('Space-War')

# Background
background = pygame.image.load('images/space.png')

# Screen
screen = pygame.display.set_mode((800, 600))
run = True

# Background_sound:
mixer.music.load('sounds/background.wav')
mixer.music.play(-1)
# Loading images
spaceship_icon = pygame.image.load('images/spaceship_icon.png')
pygame.display.set_icon(spaceship_icon)

# Player-Attributes
playerImage = pygame.image.load('images/spaceship.png')
playerX = 370
playerY = 480
velocityX = 0

# Enemy-Attributes
num_of_enemies = 6
enemyImage = []
enemyX = []
enemyY = []
enemy_changeX = []
enemy_changeY = []
for i in range(num_of_enemies):
    enemyImage.append(pygame.image.load('images/enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemy_changeX.append(1)
    enemy_changeY.append(40)

# Bullets
bullet = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bullet_velocity = 3
# States of bullet
bullet_state = 'ready'

# score
score_value = 0
font = pygame.font.Font('font/Douglas.ttf', 50)
textX = 10
textY = 10

#Game Over

over_font = pygame.font.Font('font/thunder.otf',64)


def showscore(x, y):
    score = font.render('Score:' + str(score_value), True, (255, 255, 255))
    screen.blit(score, [x, y])

def game_over_text(x,y):
    over_text = over_font.render('GAME OVER',True,(255,255,255))
    screen.blit(over_text,[200,250])


def player(x, y):
    screen.blit(playerImage, [x, y])


def enemy(x, y):
    screen.blit(enemyImage[i], [x, y])


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet, [x + 16, y + 10])


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(pow(enemyX - bulletX, 2) + (pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Main game loop:
while run:
    screen.fill((0, 0, 0))
    screen.blit(background, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Fetching keystroke events -Movement Mechanics
        # Changing velocities when key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocityX -= 5
            if event.key == pygame.K_RIGHT:
                velocityX += 5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_sound = mixer.Sound('sounds/laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        # Setting the velocity back to zero when key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                velocityX = 0

    # Changing the co-ordinates of the player
    playerX += velocityX

    # Checking boundaries
    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movements
    for i in range(num_of_enemies):
        #Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(200,250)
            break
        enemyX[i] += enemy_changeX[i]
        if enemyX[i] < 0:
            enemy_changeX[i] = 1
            enemyY[i] += enemy_changeY[i]
        elif enemyX[i] >= 736:
            enemy_changeX[i] = -1

        # Collision
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i])

    # Bullet_movement
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_velocity
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    player(playerX, playerY)
    showscore(textX, textY)
    pygame.display.update()

