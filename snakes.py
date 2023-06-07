import pygame

# Initialize the game
pygame.init()

# Set the screen size
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Create the snake
snake = []
snake.append([100, 100])
snake.append([100, 110])
snake.append([100, 120])

# Create the food
food = [300, 300]

# Set the snake speed
snake_speed = 10

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        # Quit the game if the user clicks the X button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake[0][1] > 0:
                    snake[0][1] -= snake_speed
            elif event.key == pygame.K_DOWN:
                if snake[0][1] < screen_height - 1:
                    snake[0][1] += snake_speed
            elif event.key == pygame.K_LEFT:
                if snake[0][0] > 0:
                    snake[0][0] -= snake_speed
            elif event.key == pygame.K_RIGHT:
                if snake[0][0] < screen_width - 1:
                    snake[0][0] += snake_speed

    # Update the snake position
    for i in range(len(snake) - 1):
        snake[i] = snake[i + 1]

    # Move the snake head
    snake[-1] = [snake[-1][0] + snake_speed, snake[-1][1]]

    # Check if the snake hit the food
    if snake[0] == food:
        # Grow the snake
        snake.append([snake[-1][0], snake[-1][1]])

        # Generate new food
        food = [random.randint(0, screen_width - 1), random.randint(0, screen_height - 1)]

    # Check if the snake hit itself or the edge of the screen
    for i in range(1, len(snake)):
        if snake[0] == snake[i]:
            print("Game over!")
            pygame.quit()
            exit()

    if snake[0][0] < 0 or snake[0][0] >= screen_width or snake[0][1] < 0 or snake[0][1] >= screen_height:
        print("Game over!")
        pygame.quit()
        exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    for i in range(len(snake)):
        pygame.draw.rect(screen, (255, 0, 0), (snake[i][0], snake[i][1], 10, 10))

    # Draw the food
    pygame.draw.rect(screen, (0, 255, 0), (food[0], food[1], 10, 10))

    # Update the display
    pygame.display.update()
