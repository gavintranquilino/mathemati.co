# 1. pass them in (x coord, y cord, 999, value)
import pygame
import sys


# NEW IMPORTANT CODE STARTS HERE ==================================================================================

# DEDICATED TO MIJIC!!!!!

import random

from Objects import Number
from Objects import Operations
from Objects import GarbageCan
from Objects import Squares
from Objects import Circle
from Objects import Equals
from Objects import Answer

# 2. save them elsewhere

# DEFINING ALL OF THE NUMBERS (X COORD, Y COORD, DISTANCE, VALUE OF THE NUMBER

zero = Number(15, 30, 999, 0)
one = Number(78.8, 30, 999, 1)
two = Number(142.6, 30, 999, 2)
three = Number(206.4, 30, 999, 3)
four = Number(270.2, 30, 999, 4)
five = Number(334.0, 30, 999, 5)
six = Number(397.0, 30, 999, 6)
seven = Number(461.6, 30, 999, 7)
eight = Number(525.4, 30, 999, 8)
nine = Number(590, 30, 999, 9)

# PUTTING THE NUMBERS IN A LIST

numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

# DEFINING THE OPERATIONS (X COORD, Y COORD, DISTANCE, VALUE OF THE OPERATION)


addition = Operations(226, 325, 999, "+")
subtraction = Operations(439, 325, 999, "-")

# LIST OF THE OPERATIONS
# 0 CORRESPONDS TO ADDITION
# 1 CORRESPONDS TO SUBTRACTION

operations = [addition, subtraction]


# SAVING THE COORDIANTES SO THEY CAN BE REFERENCED FOR LATER IN A SEPARATE LIST
# NUMBER OF INDEX = NUMBER REFERRING TO


original_x_values = [15, 78.8, 142.6, 206.4, 270.2, 334.0, 397.0, 461.6, 525.4, 590]
original_y_value = 30

# ORIGINAL SIGN VALUES

# 0 CORRESPODING TO ADDITION FOR BOTH LISTS
# 1 CORRESPONDS TO SUBTRACTION FOR BOTH LISTS

original_sign_x_values = [176, 389]
original_sign_y_value = 30

# SETTING THE GARBAGE CAN
garbage = GarbageCan(999)

# SETTING THE GREEN BOXES (WHERE THE NUMBERS WILL GO)

green_box_one = Squares(100, 200, 999)
green_box_two = Squares(300, 200, 999)

# SETTING THE BLUE CIRCLE (WHERE THE OPERATIONS WILL GO)
blue_circle = Circle(200, 200, 999)

# SETTING THE EQUALS SIGN
red_sign = Equals(400, 200, 999)

# Setting the answer
answer_integer = random.randint(1, 17)
answer = Answer(530, 205, 999, answer_integer)


# NEW IMPORTANT CODE ENDS HERE ==================================================================================



# PYGAME STUFF STARTS HERE ----------------------------------------------------------------------------

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movable Number")

# Set up the font
font = pygame.font.Font(None, 100)  # You can choose a font and size

# Function to display a number as an object

def display_number(number, x, y):
    text = font.render(str(number), True, (0, 0, 0))  # Render the text
    screen.blit(text, (x, y))  # Draw the text on the screen

# CREATING THE GARBAGE CAN

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  # Clear the screen


    # NEW IMPORTANT CODE STARTS HERE ==================================================================================

    # DISPLAYING THE GARBAGE CAN

    # This is the same for each of the next displays
    garbage_can = pygame.image.load(garbage.value) # Load the garbage image
    garbage_rect = garbage_can.get_rect() # Create a rectangle for pygame
    scaled_garbage = pygame.transform.scale(garbage_can, (125, 125)) # Scale the garbage image (only present here)
    screen.blit(scaled_garbage, (garbage.x, garbage.y)) # Display the garbage imaege to the screen

    # DISPLAYING THE FIRST GREEN BOX

    green_box_one_display = pygame.image.load(green_box_one.value)
    green_box_one_rect = green_box_one_display.get_rect()
    screen.blit(green_box_one_display, (green_box_one.x, green_box_one.y))

    # DISPLAYING THE SECOND GREEN BOX
    green_box_two_display = pygame.image.load(green_box_two.value)
    green_box_two_rect = green_box_two_display.get_rect()
    screen.blit(green_box_two_display, (green_box_two.x, green_box_two.y))

    # DISPLAYING THE NUMBERS
    blue_circle_display = pygame.image.load(blue_circle.value)
    blue_circle_rect = blue_circle_display.get_rect()
    screen.blit(blue_circle_display, (blue_circle.x, blue_circle.y))

    # DISPLAYING THE EQUALS SIGN
    red_sign_display = pygame.image.load(red_sign.value)
    red_sign_rect = red_sign_display.get_rect()
    screen.blit(red_sign_display, (red_sign.x, red_sign.y))

    # DISPLAYING THE ANSWER

    answer_display = font.render(str(answer.value), True, (0, 0, 0))
    screen.blit(answer_display, (answer.x, answer.y))


    
    for i in range(len(numbers)):
        display_number(numbers[i].value, numbers[i].x, numbers[i].y)

    # DISPLAYING THE OPERATIONS
        
    for i in range(len(operations)):
        display_number(operations[i].value, operations[i].x, operations[i].y)




    pygame.display.flip()  # Update the display



