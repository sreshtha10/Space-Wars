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