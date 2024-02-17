import cv2
import mediapipe as mp
import pygame
import sys
import random

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Capture Video from Webcam
cap = cv2.VideoCapture(0)
camera_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
camera_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((camera_width, camera_height))
pygame.display.set_caption("Hand Tracking with Pygame")
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game variables
finger_radius = 20
finger_pos = [camera_width // 2, camera_height // 2]  # Initial finger position
blue_dot_pos = [random.randint(0, camera_width - finger_radius), random.randint(0, camera_height - finger_radius)]  # Initial blue dot position
blue_dot_speed = 5  # Speed of the blue dot

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            pygame.quit()
            sys.exit()

    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * camera_width)
            y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * camera_height)

            finger_pos = [x, y]

            # new

            # Check if the red dot (finger) is touching the blue dot
            distance = pygame.math.Vector2(finger_pos[0] - blue_dot_pos[0], finger_pos[1] - blue_dot_pos[1]).length()
            if distance < finger_radius:
                # Update blue dot position based on the finger movement
                blue_dot_pos = finger_pos

    # Draw on Pygame screen
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, finger_pos, finger_radius)

    # NEW
    pygame.draw.circle(screen, BLUE, blue_dot_pos, finger_radius)

    pygame.display.flip()
    clock.tick(30)

cap.release()
pygame.quit()
sys.exit()
