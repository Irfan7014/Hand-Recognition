'''
  _____ ____  ____   ___  ____    ____   ___   ___  
 | ____|  _ \|  _ \ / _ \|  _ \  | ___| / _ \ / _ \ 
 |  _| | |_) | |_) | | | | |_) | |___ \| | | | (_) |IRFAN
 | |___|  _ <|  _ <| |_| |  _ <   ___) | |_| |\__, |ALAN
 |_____|_| \_\_| \_\\___/|_| \_\ |____/ \___/   /_/ LANCE
 '''

# TODO list
# Importing Libraries and Capturing the video from webcam - Done
# Adding Trackbar to change hsv values - Done
# Converting frame to HSV - Done
# Tracking hand on the basis of color provided by the user - Done
# Creating a mask to filter the values given by user and filter the frame - Done
# Inverting the pixel value for better enhanced results - Done
# Find Contours - Done
# Drawing the contour with max contour - Done
#Find Convexity detect  for counting Values and Apply Cosin method
#Bind hand gestures with keyboard keys.

# Importing Necessary Libraries
import cv2
import pyautogui as p
import numpy as np 
import math
from tkinter import *

keys = ['up', 'left', 'right', 'down', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'backspace',
'ctrl', 'delete', 'end', 'enter', 'esc', 'escape', 'home', 'insert',
'shift', 'space', 'tab']

root = Tk()
root.title("Hand Gesture Remote Key-Mapping Interface")
root.geometry('640x320')

finger2 = StringVar()
finger3 = StringVar()
finger4 = StringVar()
finger5 = StringVar()

title_label = Label(root, text="Hand Gesture Remote", font="Helvetica 16 bold italic", fg="Blue")
credits_label = Label(root, text="Created by Irfan, Alan & Lance")
finger2_label = Label(root, text="2 Fingers: ")
finger3_label = Label(root, text="3 Fingers: ")
finger4_label = Label(root, text="4 Fingers: ")
finger5_label = Label(root, text="5 Fingers: ")
finger2_dropdown = OptionMenu(root, finger2, *keys)
finger3_dropdown = OptionMenu(root, finger3, *keys)
finger4_dropdown = OptionMenu(root, finger4, *keys)
finger5_dropdown = OptionMenu(root, finger5, *keys)
ok_button = Button(root, text="Ok", command=root.quit)

title_label.grid(row=0, column=0, columnspan=5)
credits_label.grid(row=1, column=0, columnspan=4)
finger2_label.grid(row=2, column=0)
finger3_label.grid(row=3, column=0)
finger4_label.grid(row=4, column=0)
finger5_label.grid(row=5, column=0)
finger2_dropdown.grid(row=2, column=1)
finger3_dropdown.grid(row=3, column=1)
finger4_dropdown.grid(row=4, column=1)
finger5_dropdown.grid(row=5, column=1)
ok_button.grid(row=6, column=2)

root.mainloop()

fing2 = finger2.get()
fing3 = finger3.get()
fing4 = finger4.get()
fing5 = finger5.get()

# Creating the capture instance for taking frames from webcam
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# nothing function will be called continuously when the trackerbar is not used
def nothing(x):
    pass

# Giving window-name for the trackbar
cv2.namedWindow("Color Adjustments",cv2.WINDOW_NORMAL)

# Resizing the size of trackbar window
cv2.resizeWindow("Color Adjustments", (300, 300))

# Creating threshold trackbar
cv2.createTrackbar("Thresh", "Color Adjustments", 0, 255, nothing)

# Adding Trackbars for color detection
cv2.createTrackbar("Lower_H", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_S", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_V", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Upper_H", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_S", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_V", "Color Adjustments", 255, 255, nothing)

# This loop will run continuously until the user doesn't press the escape key
while True:
    iscamworking, frame = cap.read()        # Reads frame from webcam
    frame = cv2.flip(frame,2)               # Flip the frame along y axis
    frame = cv2.resize(frame,(600,500))     # To resize the fraze
    # Creating a sub window for hand, the border will be blue
    cv2.rectangle(frame, (0,1), (300,500),(0, 255, 0), 0)
    cropped_image = frame[1:500, 0:300]     # Creating a cropped image of hand
    

    hsv = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)    # Creating hsv of cropped image


    # Hand Detection values; it will take values from tracj
    l_hue = cv2.getTrackbarPos("Lower_H", "Color Adjustments")  # lower hue
    l_sat = cv2.getTrackbarPos("Lower_S", "Color Adjustments")  # lower saturation
    l_val = cv2.getTrackbarPos("Lower_V", "Color Adjustments")  # lower brightness

    u_hue = cv2.getTrackbarPos("Upper_H", "Color Adjustments")  # higher hue
    u_sat = cv2.getTrackbarPos("Upper_S", "Color Adjustments")  # high saturation
    u_val = cv2.getTrackbarPos("Upper_V", "Color Adjustments")  # higher brightness

    # Putting the values obtained from trackbar into arrays
    lower_bound = np.array([l_hue,l_sat,l_val])   # Lower Bound Values
    upper_bound = np.array([u_hue,u_sat,u_val])   # Upper Bound Values
    

    # Creating a mask to filter the values given by user and filter the frame
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Filtering the original image with mask
    filtr = cv2.bitwise_and(cropped_image, cropped_image, mask=mask)
    
    #Step - 5 Find threshold to convert greyscale image to black and white, if lower than threshold range wblack else white
    mask1  = cv2.bitwise_not(mask)      # performing bitwise not to invert black and white
    m_g = cv2.getTrackbarPos("Thresh", "Color Adjustments")     # Getting threshold value from trackbar
    ret,thresh = cv2.threshold(mask1,m_g,255,cv2.THRESH_BINARY) # adding the threshold values into bitmap
    dilated = cv2.dilate(thresh,(3,3),iterations = 6)       # Dialating the frame (remove noise from the image)
    
    # Finding contours
    cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  # finding cnt, and heirarchy
    
    try:
        # Find contour that has the maximum area
        cm = max(cnts, key=lambda x: cv2.contourArea(x))    # Finding contour with max area
        epsilon = 0.0005*cv2.arcLength(cm,True)
        data= cv2.approxPolyDP(cm,epsilon,True)
    
        hull = cv2.convexHull(cm)       # hull is the red border around the hand this is optional
        
        cv2.drawContours(cropped_image, [cm], -1, (50, 50, 150), 2) # drawing the max contour
        cv2.drawContours(cropped_image, [hull], -1, (0, 255, 0), 2) # this is optional just to see how camera catches the hand
        
        #Step - 8
        # Find convexity defects
        hull = cv2.convexHull(cm, returnPoints=False) # creating a hull
        defects = cv2.convexityDefects(cm, hull)    # finds the conexity defects in a hull
        count_defects = 0           # count convexity defects
        #print("Area==",cv2.contourArea(hull) - cv2.contourArea(cm))
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]      #start, end, far
           
            start = tuple(cm[s][0])
            end = tuple(cm[e][0])
            far = tuple(cm[f][0])
            # Performing cosine rule to find the angle
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / 3.14

            #check if it is a valid defect
            if angle <= 50:
                count_defects += 1
                cv2.circle(cropped_image,far,5,[255,255,255],-1)
        
        #Step - 9 
        # Print number of fingers
        if count_defects == 0:
            print('1 finger')
        elif count_defects == 1:
            print("2 fingers")
            p.press(fing2)
        elif count_defects == 2:
            print('3 fingers')
            p.press(fing3)
        elif count_defects == 3:
            print('4 fingers')
            p.press(fing4)
        elif count_defects == 4:
            print('5 fingers')
            p.press(fing5)
        else:
            pass
    except:
        pass

    #step -10    
    cv2.imshow("Thresh", thresh)
    #cv2.imshow("filter==",filtr)
    cv2.imshow("Result", frame)

    key = cv2.waitKey(25) &0xFF    
    if key == 27: 
        break
cap.release()
cv2.destroyAllWindows()