import cv2
import mediapipe as mp
import pygame

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
finger_pos = (screen_width // 2, screen_height // 2)  # Initial finger position

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

    # Flip the frame vertically for selfie view, and convert the BGR image to RGB.
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands.
    results = hands.process(frame)

    # If a hand is detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the coordinates of the index finger tip
            x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1])
            y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0])

            # Update finger position
            finger_pos = (x, y)

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw finger circle on Pygame screen
    pygame.draw.circle(screen, RED, finger_pos, finger_radius)

    # Update Pygame display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Release the webcam and quit Pygame
cap.release()
pygame.quit()
