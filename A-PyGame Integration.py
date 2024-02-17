import cv2
import mediapipe as mp
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up Pygame window
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hand Tracking with Pygame")

# Set up Mediapipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Pygame colors
black = (0, 0, 0)
white = (255, 255, 255)

y_offset = 0

# Main loop
running = True
cap = cv2.VideoCapture(0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # Capture video frame
    ret, frame = cap.read()

    # Rotate and flip the frame
    frame = cv2.transpose(frame)

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            for landmark in landmarks.landmark:
                # Extract hand coordinates
                x, y = int(landmark.x * width), int((landmark.y * height) + y_offset)

                # Draw a circle at each hand landmark
                cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

    # Convert the frame to RGB for Pygame display
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pygame_frame = pygame.surfarray.make_surface(frame_rgb)

    # Draw the frame on the Pygame window
    window.blit(pygame_frame, (0, 0))
    pygame.display.flip()

    # Check for the 'ESC' key or 'Q' key to exit the loop
    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        running = False

# Release resources
cap.release()
cv2.destroyAllWindows()
pygame.quit()
sys.exit()
