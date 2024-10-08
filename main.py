import cv2
import mediapipe as mp
from Objects import *
from Frontend import *
import random

# ------------------------Game STUFF--------------------#
score = 0
left = None
right = None
correct = False

# need to initialize a random one first
sign_integer = random.randint(0, 1)
if sign_integer == 0:
    sign = "+"
else:
    sign = "-"

n = 3  # number of each number

# SETTING THE NUMBERS
zeros, zero_orig = [Number(15, 30, 999, 0) for i in range(n)], \
    [15 for i in range(n)]
ones, ones_orig = [Number(78.8, 30, 999, 1) for i in range(n)], \
    [79 for i in range(n)]
twos, twos_orig = [Number(142.6, 30, 999, 2) for i in range(n)], \
    [143 for i in range(n)]
threes, threes_orig = [Number(206.4, 30, 999, 3) for i in range(n)], \
    [207 for i in range(n)]
fours, fours_orig = [Number(270.2, 30, 999, 4) for i in range(n)], \
    [270 for i in range(n)]
fives, fives_orig = [Number(334.0, 30, 999, 5) for i in range(n)], \
    [334 for i in range(n)]
sixes, sixes_orig = [Number(397.0, 30, 999, 6) for i in range(n)], \
    [397 for i in range(n)]
sevens, sev_orig = [Number(461.6, 30, 999, 7) for i in range(n)], \
    [462 for i in range(n)]
eights, eight_orig = [Number(525.4, 30, 999, 8) for i in range(n)], \
    [525 for i in range(n)]
nines, nines_orig = [Number(590, 30, 999, 9) for i in range(n)], \
    [590 for i in range(n)]

# PUTTING THE NUMBERS IN A LIST
numbers = zeros + ones + twos + threes + fours + fives + sixes + sevens + eights + nines

# SAVING THE COORDIANTES SO THEY CAN BE REFERENCED FOR LATER IN A SEPARATE LIST
# NUMBER OF INDEX = NUMBER REFERRING TO
original_x_values = zero_orig + ones_orig + twos_orig + threes_orig + \
                    fours_orig + fives_orig + sixes_orig + sev_orig + eight_orig + nines_orig
assert len(original_x_values) == len(numbers)

original_y_value = 30

# SETTING THE GARBAGE CAN
garbage = GarbageCan(999)

# SETTING THE GREEN BOXES (WHERE THE NUMBERS WILL GO)
green_box_one = Squares(100, 200, 999)
green_box_two = Squares(300, 200, 999)

# SETTING THE BLUE CIRCLE (WHERE THE OPERATIONS WILL GO)
blue_circle = Circle(200, 200, 999)

# SETTING THE EQUALS SIGN
red_sign = Equals(400, 200, 999)

operation = Operations(220, 200, 999, sign)

# Setting the answer
answer_integer = random.randint(1, 9)
answer = Answer(530, 205, 999, answer_integer)


def get_hand_pos(results, mp_hands, frame, mp_drawing) -> tuple[
                                                              int, int] | None:
    """
    Returns the coordinates of the hand position
    """

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for lm in hand_landmarks.landmark:
                mp_drawing.draw_landmarks(frame, hand_landmarks,
                                          mp_hands.HAND_CONNECTIONS)
            x = int(hand_landmarks.landmark[
                        mp_hands.HandLandmark.INDEX_FINGER_TIP].x *
                    frame.shape[
                        1])
            y = int(hand_landmarks.landmark[
                        mp_hands.HandLandmark.INDEX_FINGER_TIP].y *
                    frame.shape[
                        0])
        return (x, y)


def restart(correct: bool):
    global score, left, right, operation, answer

    answer_int = random.randint(1, 9)
    answer.value = answer_int
    if correct:
        for i in range(len(numbers)):
            num = numbers[i]
            num.x, num.y = original_x_values[i], original_y_value

        score += 1
        left = right = None

        sign_int = random.randint(0, 1)
        if sign_int == 0:
            sin = "+"
        else:
            sin = "-"
        operation.value = sin
    else:
        for i in range(len(numbers)):
            num = numbers[i]
            num.x, num.y = original_x_values[i], original_y_value

        score = max(0, score - 1)
        left = right = None

        sign_int = random.randint(0, 1)
        if sign_int == 0:
            sin = "+"
        else:
            sin = "-"
        operation.value = sin


def main() -> None:
    global left, right, operation, score
    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    # Initialize Pygame
    # pygame.init()
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    # Define color red and background image
    RED = (255, 0, 0)
    background_image = pygame.image.load('math background.jpg')
    background = pygame.transform.scale(background_image,
                                        (screen_width, screen_height))

    GRAB_DISTANCE = 20

    # Game variables
    finger_radius = 20

    # Capture Video from Webcam
    cap = cv2.VideoCapture(0)

    is_grab = False  # did we grab anything? no...initially
    grabbed_object = None  # what did we grab??

    while True:
        # Check for Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()

        # screen.blit(background, (0, 0))
        screen.fill((255, 255, 255))
        display_green_box(green_box_one, screen)
        display_green_box(green_box_two, screen)
        display_equals(red_sign, screen)
        display_answer(answer, screen)
        display_operation(operation, screen)
        display_garbage(garbage, screen)
        display_numbers(numbers, screen)
        display_value(score, screen)

        ret, frame = cap.read()
        if ret:
            # Flip the frame vertically for selfie view, and convert the BGR image to RGB.
            frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

            # Process the frame with MediaPipe Hands.
            results = hands.process(frame)
            finger_pos = get_hand_pos(results, mp_hands, frame,
                                      mp.solutions.drawing_utils)

            if finger_pos:
                pygame.draw.circle(screen, RED, finger_pos, finger_radius)
                print(finger_pos)

                # GRAB LOGIC
                if is_grab:
                    grabbed_object.x, grabbed_object.y = finger_pos[0], \
                        finger_pos[1]

                    # ------------------------DROPPING-----------------#
                    # if finger_pos[0] and finger_pos[1] are within the green box, print "in green box"
                    if (green_box_one.x < finger_pos[
                        0] < green_box_one.x + 100 and green_box_one.y <
                            finger_pos[1] < green_box_one.y + 100):
                        print("in green box one")
                        # set the coordinates of the grabbed object to the coordinates of the green box and set is_grab to False
                        grabbed_object.x, grabbed_object.y = green_box_one.x, green_box_one.y
                        left = grabbed_object.value
                        is_grab = False
                    elif (green_box_two.x < finger_pos[
                        0] < green_box_two.x + 100 and green_box_two.y <
                          finger_pos[1] < green_box_two.y + 100):
                        print("in green box two")
                        # set the coordinates of the grabbed object to the coordinates of the green box and set is_grab to False
                        grabbed_object.x, grabbed_object.y = green_box_two.x, green_box_two.y
                        right = grabbed_object.value
                        is_grab = False
                    elif (garbage.x < finger_pos[
                        0] < garbage.x + 125 and garbage.y < finger_pos[
                              1] < garbage.y + 125):
                        grabbed_object.x, grabbed_object.y = original_x_values[
                            3 * grabbed_object.value], original_y_value
                        is_grab = False

                else:
                    for obj in numbers:
                        is_grab = obj.grab(finger_pos[0], finger_pos[1],
                                           GRAB_DISTANCE)
                        # print(is_grab)
                        if is_grab:
                            grabbed_object = obj
                            break
        if left is not None and right is not None:
            if operation.value == '+':
                lhs = left + right
                rhs = answer.value
                restart(lhs == rhs)
            else:
                lhs = left - right
                rhs = answer.value
                restart(lhs == rhs)

        # Draw the opencv image onto pygame window
        # resize opencv to be 1/8 of the pygame window size, and display on the bottom right
        frame = cv2.resize(frame, (screen_width // 4, screen_height // 4))
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        frame = cv2.flip(frame, 1)

        screen.blit(pygame.surfarray.make_surface(frame),
                    (screen_width * 0.75, screen_height * 0.75))

        # ------------------------Adam's drawings replace this-----------------#
        for obj in numbers:
            pygame.draw.circle(screen, (0, 0, 255), (obj.x, obj.y), 1)
        # ----------------------------------------------------------------------#

        # Update the display
        pygame.display.flip()

        clock.tick(55)

    # Release the webcam and quit Pygame
    cap.release()
    pygame.quit()


if __name__ == "__main__":

    main()
