import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        continue
    
    # Get the frame dimensions
    height, width, _ = frame.shape

    # Calculate the side length for a square frame
    side_length = min(height, width)

    # Calculate the cropping region
    top = (height - side_length) // 2
    bottom = top + side_length
    left = (width - side_length) // 2
    right = left + side_length

    # Crop the frame to make it square
    frame = frame[top:bottom, left:right]

    # Calculate the thirds of the frame
    first_third = side_length // 3
    second_third = (side_length // 3) * 2

    # Create the lines that form the 3x3 grid
    line1 = ((first_third, 0), (first_third, side_length))
    line2 = ((second_third, 0), (second_third, side_length))
    line3 = ((0, first_third), (side_length, first_third))
    line4 = ((0, second_third), (side_length, second_third))

    # Draw the lines to form the 3x3 grid
    cv2.line(frame, line1[0], line1[1], (0, 255, 0), 2)
    cv2.line(frame, line2[0], line2[1], (0, 255, 0), 2)
    cv2.line(frame, line3[0], line3[1], (0, 255, 0), 2)
    cv2.line(frame, line4[0], line4[1], (0, 255, 0), 2)

    # Convert the BGR image to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert the grayscale frame to RGB
    frame_rgb = cv2.cvtColor(frame_gray, cv2.COLOR_GRAY2RGB)

    # Process the frame for hand landmarks
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Iterate through the landmarks of a single hand
            for landmark_id, landmark in enumerate(hand_landmarks.landmark):
                # Get the X and Y coordinates of the landmark
                x = landmark.x 
                y = landmark.y

                if x < 1/3 and y < 1/3:
                    print('Up-Left')
                elif x < 1/3 and y < 2/3:
                    print('Left')
                elif x < 1/3 and y <= 1:
                    print('Down-Left')
                elif x < 2/3 and y < 1/3:
                    print('Up')
                elif x < 2/3 and y < 2/3:
                    print('Center')
                elif x < 2/3 and y <= 1:
                    print('Down')
                elif x <= 1 and y < 1/3:
                    print('Up-Right')
                elif x <= 1 and y < 2/3:
                    print('Right')
                elif x <= 1 and y <= 1:
                    print('Down-Right')


    # Display the square frame with hand landmarks
    cv2.imshow('MediaPipe Hands', frame)

    if cv2.waitKey(10) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
