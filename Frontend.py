# 1. pass them in (x coord, y cord, 999, value)
import pygame

# import sys

# # DEDICATED TO MIJIC!!!!!

# PYGAME STUFF STARTS HERE ----------------------------------------------------------------------------

# Set up the font
pygame.init()
font = pygame.font.Font(None, 100)  # You can choose a font and size


# Function to display a number as an object

def display_number(number, x, y, screen):
    text = font.render(str(number), True, (0, 0, 0))  # Render the text
    screen.blit(text, (x, y))  # Draw the text on the screen


def display_numbers(numbers, screen):
    for i in range(len(numbers)):
        display_number(numbers[i].value, numbers[i].x, numbers[i].y, screen)


# # This is the same for each of the next displays
# garbage_can = pygame.image.load(garbage.value) # Load the garbage image
# garbage_rect = garbage_can.get_rect() # Create a rectangle for pygame
# scaled_garbage = pygame.transform.scale(garbage_can, (125, 125)) # Scale the garbage image (only present here)
# screen.blit(scaled_garbage, (garbage.x, garbage.y)) # Display the garbage imaege to the screen
# display the garbage can as a function
def display_garbage(garbage, screen):
    garbage_can = pygame.image.load(garbage.value)  # Load the garbage image
    garbage_rect = garbage_can.get_rect()  # Create a rectangle for pygame
    scaled_garbage = pygame.transform.scale(garbage_can, (
    125, 125))  # Scale the garbage image (only present here)
    screen.blit(scaled_garbage, (
    garbage.x, garbage.y))  # Display the garbage imaege to the screen


# DISPLAYING THE FIRST GREEN BOX

def display_green_box(green_box, screen):
    green_box_display = pygame.image.load(green_box.value)
    green_box_rect = green_box_display.get_rect()
    screen.blit(green_box_display, (green_box.x, green_box.y))


# # DISPLAYING THE SECOND GREEN BOX
# green_box_two_display = pygame.image.load(green_box_two.value)
# green_box_two_rect = green_box_two_display.get_rect()
# screen.blit(green_box_two_display, (green_box_two.x, green_box_two.y))

# # DISPLAYING THE NUMBERS
# blue_circle_display = pygame.image.load(blue_circle.value)
# blue_circle_rect = blue_circle_display.get_rect()
# screen.blit(blue_circle_display, (blue_circle.x, blue_circle.y))

# # DISPLAYING THE EQUALS SIGN
# red_sign_display = pygame.image.load(red_sign.value)
# red_sign_rect = red_sign_display.get_rect()
# screen.blit(red_sign_display, (red_sign.x, red_sign.y))
# display equal sign as a function
def display_equals(equals, screen):
    equals_display = pygame.image.load(equals.value)
    equals_rect = equals_display.get_rect()
    screen.blit(equals_display, (equals.x, equals.y))


# # DISPLAYING THE ANSWER

# display the value on pygame screen given a int value and screen
def display_value(value, screen):
    value_display = pygame.font.Font(None, 80).render("Score:" + str(value),
                                                      True, (0, 0, 0))
    screen.blit(value_display, (180, 360))


# answer_display = font.render(str(answer.value), True, (0, 0, 0))
# screen.blit(answer_display, (answer.x, answer.y))
# display the answer as a function
def display_answer(answer, screen):
    answer_display = font.render(str(answer.value), True, (0, 0, 0))
    screen.blit(answer_display, (answer.x, answer.y))


# display the operation as a function
def display_operation(operation, screen):
    operation_display = font.render(str(operation.value), True, (0, 0, 0))
    screen.blit(operation_display, (operation.x, operation.y))


# DISPLAYING THE OPERATIONS

def display_operations(operations, screen):
    for i in range(len(operations)):
        operations_display = font.render(str(operations[i].value), True,
                                         (0, 0, 0))
        screen.blit(operations_display, (operations[i].x, operations[i].y))
