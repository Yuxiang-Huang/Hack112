import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        #most of the weird stuff here is normal opencv jargon.. etc
        ret, frame = cap.read()

        #fliping image
        frame = cv2.flip(frame, 1)

        #BGR to RGB since mediapipe only works with rgb
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #set flag
        image.flags.writeable = False

        #detections
        results = hands.process(image)
        
        #setting flag to true
        image.flags.writeable = True

        #RGB to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        #frame dimensions
        height, width, _ = frame.shape

        #getting fractions to use for line dimensions
        x_seventh = width // 7
        y_thirds = height // 3

        #vertical lines for player 1
        line1 = ((x_seventh, 0), (x_seventh, height))
        line2 = ((x_seventh * 2, 0), (x_seventh * 2, height))
        line3 = ((x_seventh * 3, 0), (x_seventh * 3, height))

        #vertical lines for player 2
        line4 = ((x_seventh * 4, 0), (x_seventh * 4, height))
        line5 = ((x_seventh * 5, 0), (x_seventh * 5, height))
        line6 = ((x_seventh * 6, 0), (x_seventh * 6, height))

        #horizontal lines
        line7 = ((0, y_thirds), (x_seventh * 3, y_thirds))
        line8 = ((0, y_thirds * 2), (x_seventh * 3, y_thirds * 2))
        line9 = ((x_seventh * 4, y_thirds), (width, y_thirds))
        line10 = ((x_seventh * 4, y_thirds * 2), (width, y_thirds * 2))
        
        #vertical lines
        cv2.line(frame, line1[0], line1[1], (0, 255, 0), 4)
        cv2.line(frame, line2[0], line2[1], (0, 255, 0), 4)
        cv2.line(frame, line3[0], line3[1], (0, 255, 0), 4)

        cv2.line(frame, line4[0], line4[1], (0, 255, 0), 4)
        cv2.line(frame, line5[0], line5[1], (0, 255, 0), 4)
        cv2.line(frame, line6[0], line6[1], (0, 255, 0), 4)

        #horizontal lines
        cv2.line(frame, line7[0], line7[1], (0, 255, 0), 4)
        cv2.line(frame, line8[0], line8[1], (0, 255, 0), 4)
        cv2.line(frame, line9[0], line9[1], (0, 255, 0), 4)
        cv2.line(frame, line10[0], line10[1], (0, 255, 0), 4)

        #overlaying skeleton and checking for fingers up
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), 
                                                                 thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), 
                                                                 thickness=2, circle_radius=2),
                                          )

                #calculating write x coordinate(landmark 0)
                #results.multi_hand_landmarks is a weird non-comma separated list
                #that i spent a while figuring out and reading about to get the
                #wrist landmark for below. the x coord is also given
                #in a value 0-1, so i had to times it by the width
                wrist_x = int(hand_landmarks.landmark[0].x * width)

                #counting the # of extended fingers, needs 4 for powerup
                #ranges from 8,12,16,20 because those re the tips of the finger
                finger_states = [int(hand_landmarks.landmark[i].y < 
                                     hand_landmarks.landmark[i - 2].y) 
                                     for i in range(8, 21, 4)]

                if wrist_x < width / 2:  #left half-player 1
                    if sum(finger_states) == 4:
                        print('Power-Up-Player1')
                else:  #right half-player 2
                    if sum(finger_states) == 4:
                        print('Power-Up-Player2')
    
        #getting Area
        if results.multi_hand_landmarks:
            # print(results.multi_hand_landmarks)
            for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
                for landmark in hand_landmarks.landmark:
                    x = landmark.x
                    y = landmark.y
                    
                    if 0 <= x <= 1/7 and 0 <= y <= 1/3:
                        print('Up-Left-Player2')
                    elif 1/7 <= x <= 2/7 and 0 <= y <= 1/3:
                        print('Up-Player1')
                    elif 2/7 <= x <= 3/7 and 0 <= y <= 1/3:
                        print('Up-Right-Player1')

                    elif 0 <= x <= 1/7 and 1/3 <= y <= 2/3:
                        print('Left-Player1')
                    elif 1/7 <= x <= 2/7 and 1/3 <= y <= 2/3:
                        print('Center-Player1')
                    elif 2/7 <= x <= 3/7 and 1/3 <= y <= 2/3:
                        print('Right-Player1')
                    
                    elif 0 <= x <= 1/7 and 2/3 <= y <= 1:
                        print('Down-Left-Player1')
                    elif 1/7 <= x <= 2/7 and 2/3 <= y <= 1:
                        print('Down-Player1')
                    elif 2/7 <= x <= 3/7 and 2/3 <= y <= 1:
                        print('Down-Right-Player1')

                    elif 4/7 <= x <= 5/7 and 0 <= y <= 1/3:
                        print('Up-Left-Player2')
                    elif 5/7 <= x <= 6/7 and 0 <= y <= 1/3:
                        print('Up-Player2')
                    elif 6/7 <= x <= 1 and 0 <= y <= 1/3:
                        print('Up-Right-Player2')

                    elif 4/7 <= x <= 5/7 and 1/3 <= y <= 2/3:
                        print('Left-Player2')
                    elif 5/7 <= x <= 6/7 and 1/3 <= y <= 2/3:
                        print('Center-Player2')
                    elif 6/7 <= x <= 1 and 1/3 <= y <= 2/3:
                        print('Right-Player2')
                    
                    elif 4/7 <= x <= 5/7 and 2/3 <= y <= 1:
                        print('Down-Left-Player2')
                    elif 5/7 <= x <= 6/7 and 2/3 <= y <= 1:
                        print('Down-Player2')
                    elif 6/7 <= x <= 1 and 2/3 <= y <= 1:
                        print('Down-Right-Player2')
                    
                    break
                        
        cv2.imshow('Hand Tracking', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
