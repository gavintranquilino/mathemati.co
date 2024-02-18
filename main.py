import cv2
import mediapipe as mp
import pygame
from Objects import Number, Operations, GarbageCan


def get_hand_pos(results, mp_hands, frame, mp_drawing) -> tuple[int] | None:
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

def main():
    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    # Initialize Pygame
    pygame.init()
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
    '''finger_pos = (
    screen_width // 2, screen_height // 2)  # Initial finger position'''

    # Capture Video from Webcam
    cap = cv2.VideoCapture(0)

    # ---------------------will be replaced by adam's code------------------#
    test_object = Number(300, 300, 30, 1)
    test_object2 = Number(100, 100, 30, 1)
    test_object3 = Number(346, 337, 30, 1)

    object_list = [test_object, test_object2, test_object3]
    # ----------------------------------------------------------------------#

    is_grab = False  # did we grab anything? no...initially
    grabbed_object = None  # what did we grab??

    while True:
        # Check for Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()

        screen.blit(background, (0, 0))

        ret, frame = cap.read()
        if ret:
            # Flip the frame vertically for selfie view, and convert the BGR image to RGB.
            frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

            # Process the frame with MediaPipe Hands.
            results = hands.process(frame)
            finger_pos = get_hand_pos(results, mp_hands, frame, mp.solutions.drawing_utils)
            if finger_pos:
                pygame.draw.circle(screen, RED, finger_pos, finger_radius)
                # print(finger_pos)

                # GRAB LOGIC
                if is_grab:
                    grabbed_object.x, grabbed_object.y = finger_pos[0], \
                        finger_pos[1]

                else:
                    for obj in object_list:
                        is_grab = obj.grab(finger_pos[0], finger_pos[1],
                                           GRAB_DISTANCE)
                        print(is_grab)
                        if is_grab:
                            grabbed_object = obj
                            break

        # ------------------------Adam's drawings replace this-----------------#
        for obj in object_list:
            pygame.draw.circle(screen, (0, 0, 255), (obj.x, obj.y), 30)
        # ----------------------------------------------------------------------#

        # Draw a red circle representing the finger
        pygame.display.flip()
        cv2.imshow('MediaPipe Hands', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        cv2.waitKey(1)
        clock.tick(30)

    # Release the webcam and quit Pygame
    cap.release()
    pygame.quit()

if __name__ == "__main__":
    main()