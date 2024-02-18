import cv2
import mediapipe as mp
import pygame


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


def main():
    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    # Initialize Pygame
    pygame.init()
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Game variables
    finger_radius = 20
    finger_pos = (
    screen_width // 2, screen_height // 2)  # Initial finger position

    # Capture Video from Webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Check for Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()

        # Fill the screen with white color
        screen.fill(WHITE)

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
