import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display - NOT NEEDED
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movable Number")

# Set up the font
patrick = pygame.font.Font(None, 100)  # You can choose a font and size - the number changes the size of the number


# ABOVE LINE CREATES THE FONT


# Function to display a number as an object
def display_number(x, y):
    text = patrick.render(str(1), True, (0, 0, 0))  # Render the text
    screen.blit(text, (x, y))  # Draw the text on the screen

# Initial position of the number
number_x, number_y = 100, 100

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  # Clear the screen

    # Get the position of the mouse cursor
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check if the mouse cursor is within the bounding box of the number
    if number_x < mouse_x < number_x + 36 and number_y < mouse_y < number_y + 36:
        # Check for mouse click events
        if pygame.mouse.get_pressed()[0]:  # Left mouse button
            dragging = True
            offset_x = mouse_x - number_x
            offset_y = mouse_y - number_y

    # Check for mouse release events
    if not pygame.mouse.get_pressed()[0]:
        dragging = False

    # Update the position of the number if dragging
    if dragging:
        number_x, number_y = mouse_x - offset_x, mouse_y - offset_y

    # Display the number at the updated position
    display_number(number_x, number_y)

    pygame.display.flip()  # Update the display
