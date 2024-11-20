import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width, window_height = 800, 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Move the Square")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define square properties
square_size = 50
x, y = window_width // 2, window_height // 2
speed = 5

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Fill the screen with black
    window.fill(black)

    # Draw the square
    pygame.draw.rect(window, white, (x, y, square_size, square_size))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    pygame.time.Clock().tick(80)

# Quit Pygame
pygame.quit()
