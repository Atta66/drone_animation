import pygame

# Initialize pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)  # Added



# Define the size of each cell in the grid
CELL_SIZE = 50

# Define the size of the window
WINDOW_SIZE = CELL_SIZE * 9

def move_drone(x, y):
    # Convert grid coordinates to pixel coordinates
    x_pixel = x * CELL_SIZE
    y_pixel = y * CELL_SIZE

    # Set the center of the image rectangle to the center of the cell
    drone_rect.center = (x_pixel + CELL_SIZE / 2, y_pixel + CELL_SIZE / 2)

    # Draw the image on the screen
    screen.blit(drone, drone_rect)

    # Return None
    return None

# Create the display surface
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# Set the title of the window
pygame.display.set_caption("Tunnel")


# Load the image
drone = pygame.image.load("drone.png") # Added

drone = pygame.transform.scale(drone, (CELL_SIZE, CELL_SIZE)) # Added

prev_x, prev_y = [4,8]

# Get the size of the image
drone_rect = drone.get_rect() # Added

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# # Main program loop
# if not done:
# Process events (keystrokes, mouse clicks, etc)
for event in pygame.event.get():
    # User clicked close
    if event.type == pygame.QUIT:
        # Flag that we are done so we exit this loop
        done = True

    # Set the screen background to white
if not done:

    screen.fill(WHITE)

    # Draw the grid lines
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        for y in range(0, WINDOW_SIZE, CELL_SIZE):

            if x == CELL_SIZE * 4:  # Added
                # Fill the rectangle with grey color
                pygame.draw.rect(
                    screen, GREY, [x, y, CELL_SIZE, CELL_SIZE])  # Changed

            if y == CELL_SIZE * 3:

                pygame.draw.rect(
                    screen, GREY, [x, y, CELL_SIZE, CELL_SIZE])  # Changed
            
            if x == CELL_SIZE * 4 and y == CELL_SIZE * 8: # Added
                # Set the center of the image rectangle to the center of the cell
                drone_rect.center = (x + CELL_SIZE / 2, y + CELL_SIZE / 2) # Added
                # Draw the image on the screen
                screen.blit(drone, drone_rect) # Added

            else:
                # Draw a rectangle outline
                pygame.draw.rect(
                    screen, BLACK, [x, y, CELL_SIZE, CELL_SIZE], 1)

    # pygame.display.flip()

    pygame.display.update([0, 0, WINDOW_SIZE, WINDOW_SIZE])

    pygame.time.delay(1000)

    pygame.draw.rect(screen, GREY, [prev_x * CELL_SIZE, prev_y * CELL_SIZE, CELL_SIZE, CELL_SIZE]) # Added
    
    pygame.display.update([prev_x * CELL_SIZE, prev_y * CELL_SIZE, CELL_SIZE, CELL_SIZE])
    
    pygame.time.delay(1000)

    move_drone(5, 3)
    # Update the screen with what we've drawn
    pygame.display.flip()

    # Limit to 60 frames per second
    # clock.tick(60)
    pygame.display.update([5 * CELL_SIZE , 3 * CELL_SIZE , CELL_SIZE , CELL_SIZE])

    pygame.time.delay(1000)

# Close the window and quit
# pygame.quit()


