import cv2
import mediapipe as mp
import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def main():
    # Game variables
    screen_width, screen_height = 640, 480
    finger_radius = 20
    finger_pos = (screen_width // 2, screen_height // 2)  # Initial finger position

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands()

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    # Capture Video from Webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Check for Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()

        # Capture frame from Webcam
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.flip(frame, 1)

        # Process the frame with MediaPipe Hands.
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # If a hand is detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for lm in hand_landmarks.landmark:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1])
                # y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0])
                # finger_pos = (x, y)

        # Fill the screen with white color
        screen.fill(WHITE)

        # Draw finger circle on Pygame screen
        pygame.draw.circle(screen, RED, finger_pos, finger_radius)

        cv2.imshow('MediaPipe Hands', frame)
        cv2.waitKey(1)

        # Cap the frame rate
        clock.tick(30)

    # Release the webcam and quit Pygame
    cap.release()
    pygame.quit()

if __name__ == "__main__":
    main()
