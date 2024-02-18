import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display - NOT NEEDED
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movable Number")

# Set up the font
Font = pygame.font.Font(None, 100)  # You can choose a font and size - the number changes the size of the number


# ABOVE LINE CREATES THE FONT


# Function to display a number as an object
def display_number(number, x, y):
    text = Font.render(str(number), True, (0, 0, 0))  # Render the text
    screen.blit(text, (x, y))  # Draw the text on the screen

def distances(mouse_x, mouse_y, x_positions, y_positions):
    # return the smallest distance and edit those values

    # dist list is a list with all of the different distances from each number
    dist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(x_positions)):

        # calculate the distance for one of the individual values

        dist[i] = (pygame.math.Vector2(mouse_x - x_positions[i], mouse_y - y_positions[i]).length())

        # print(i, dist[i])

    # find the lowest distance of the distances

    for i in range(len(dist) - 1):
        if dist[i] < dist[i+1]:
            lowest_index = i
        else:
            lowest_index = i+1

    return lowest_index


# Initial position of the number

# number_x, number_y = 50, 50
number_x = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
number_y = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]

offset_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
offset_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  # Clear the screen

    # Get the position of the mouse cursor
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # get the shortest distance away
    change = distances(mouse_x, mouse_y, number_x, number_y)

    # Check if the mouse cursor is within the bounding box of the number

    # needs to change to be the number you want - the one with the lowest distance

    # need to somehow code the distance to the lowest distance


    if number_x[change] < mouse_x < number_x[change] + 36 and number_y[change] < mouse_y < number_y[change] + 36:
        # Check for mouse click events
        if pygame.mouse.get_pressed()[0]:  # Left mouse button
            dragging = True
            offset_x[change] = mouse_x - number_x[change]
            offset_y[change] = mouse_y - number_y[change]

    # Check for mouse release events
    if not pygame.mouse.get_pressed()[0]:
        dragging = False

    # Update the position of the number if dragging
    if dragging:
        number_x[change], number_y[change] = mouse_x - offset_x[change], mouse_y - offset_y[change]

    # Display the number at the updated position
    display_number(0, number_x[0], number_y[0])
    display_number(1, number_x[1], number_y[1])
    display_number(2, number_x[2], number_y[2])
    display_number(3, number_x[3], number_y[3])
    display_number(4, number_x[4], number_y[4])
    display_number(5, number_x[5], number_y[5])
    display_number(6, number_x[6], number_y[6])
    display_number(7, number_x[7], number_y[7])
    display_number(8, number_x[8], number_y[8])
    display_number(9, number_x[9], number_y[9])

    pygame.display.flip()  # Update the display
