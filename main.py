if enemyY[i] > 440:
    for j in range(num_of_enemies):
        enemyY[j] = 2000
    game_over_text(200, 250)
    break

# Enemy movements
for i in range(num_of_enemies):
    # Game Over
    if enemyY[i] > 440:
        for j in range(num_of_enemies):
            enemyY[j] = 2000
        game_over_text(200, 250)
        break

# Enemy movements
for i in range(num_of_enemies):
    # Game Over
    if enemyY[i] > 440:
        for j in range(num_of_enemies):
            enemyY[j] = 2000
        game_over_text(200, 250)
        break