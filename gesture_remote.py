'''
  _____ ____  ____   ___  ____    ____   ___   ___  
 | ____|  _ \|  _ \ / _ \|  _ \  | ___| / _ \ / _ \ 
 |  _| | |_) | |_) | | | | |_) | |___ \| | | | (_) |IRFAN
 | |___|  _ <|  _ <| |_| |  _ <   ___) | |_| |\__, |ALAN
 |_____|_| \_\_| \_\\___/|_| \_\ |____/ \___/   /_/|LANCE
 '''
# Select Application To Be Used
# Key Mapping using tkinter
# Importing Libraries and Capturing the video from webcam
# Adding Trackbar to change hsv values
# Converting frame to HSV
# Tracking hand on the basis of color provided by the user
# Creating a mask to filter the values given by user and filter the frame
# Inverting the pixel value for better enhanced results
# Find Contours
# Drawing the contour with max contour
#Find Convexity detect  for counting Values and Apply Cosin method
#Bind hand gestures with keyboard keys.

#Import required libraries
import cv2  #For hand detection
import numpy as np #To store 2D array of intensity
import math #To find cosine
import pyautogui as p  #To press a keyboard key
from tkinter import *  #For beginning gui
#If user selects wasd key mapping mainly used for games
#Close window and map keys
def wasdMapping():
    global fing2, fing3, fing4, fing5
    root.destroy()
    fing2="w"
    fing3="d"
    fing4="s"
    fing5="a"
    print("'{}','{}','{}','{}'".format(fing2,fing3,fing4,fing5))
#If user selects powerpoint as the application
#Close window and map keys
def powerpointMapping():
    global fing2, fing3, fing4, fing5
    root.destroy()
    fing2="up"
    fing3="down"
    fing4="left"
    fing5="right"
    print("'{}','{}','{}','{}'".format(fing2,fing3,fing4,fing5))
#If user selects vlc media player or any other as the application
#Close window and map keys
def vlcmediaMapping():
    global fing2, fing3, fing4, fing5
    root.destroy()
    fing2="space"
    fing3="up"
    fing4="down"
    fing5="right"
    print("'{}','{}','{}','{}'".format(fing2,fing3,fing4,fing5))
#If user wants to custom map keys
#Close window and open new window to map keys
def customMapping():
    root.destroy()
    #A list of available keys to select from
    keys = ['up', 'left', 'right', 'down', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'backspace',
    'ctrl', 'delete', 'end', 'enter', 'esc', 'escape', 'home', 'insert',
    'shift', 'space', 'tab']
    window=Tk()
    window.title("Map Keys To Fingers")
    window.geometry("600x600")
    window.config(bg="#292929")
    finger2=StringVar(window)
    finger3=StringVar(window)
    finger4=StringVar(window)
    finger5=StringVar(window)

    #Title Label to display on screen
    titleLabel=Label(window,text="SET KEY BINDINGS",font="Helvetice 20 bold",bg="#292929",fg="#03DAC6").place(x=145,y=10)
    finger2_label=Label(window,text="2 Fingers: ",font="Helvetica 16 bold italic",bg="#292929",fg="#03DAC6").place(x=10,y=70)
    #Dropdown menu to select key mapping if 2 fingers are detected
    fingers2_option=OptionMenu(window, finger2, *keys)
    fingers2_option.place(x=180,y=70)
    fingers2_option.config(font="Helvetica 18 bold",height="1",width="8",bg="#292929",fg="#03DAC6")

    #Dropdown menu to select key mapping if 3 fingers are detected
    finger3_label=Label(window,text="3 Fingers: ",font="Helvetica 16 bold italic",bg="#292929",fg="#03DAC6").place(x=10,y=175)
    fingers3_option=OptionMenu(window, finger3, *keys)
    fingers3_option.place(x=180,y=175)
    fingers3_option.config(font="Helvetica 18 bold",height="1",width="8",bg="#292929",fg="#03DAC6")

    #Dropdown menu to select key mapping if 4 fingers are detected
    finger4_label=Label(window,text="4 Fingers: ",font="Helvetica 16 bold italic",bg="#292929",fg="#03DAC6").place(x=10,y=280)
    fingers4_option=OptionMenu(window, finger4, *keys)
    fingers4_option.place(x=180,y=280)
    fingers4_option.config(font="Helvetica 18 bold",height="1",width="8",bg="#292929",fg="#03DAC6")

    #Dropdown menu to select key mapping if 5 fingers are detected
    finger5_label=Label(window,text="5 Fingers: ",font="Helvetica 16 bold italic",bg="#292929",fg="#03DAC6").place(x=10,y=385)
    fingers5_option=OptionMenu(window, finger5, *keys)
    fingers5_option.place(x=180,y=385)
    fingers5_option.config(font="Helvetica 18 bold",height="1",width="8",bg="#292929",fg="#03DAC6")

    #Confirm mapped keys, close windows and open the cameras
    btnConfirm=Button(window,text="SET",command=lambda: setbindings(finger2, finger3, finger4, finger5, window))
    btnConfirm.place(x=220,y=490)
    btnConfirm.config(font="Helvetica 18 bold", width="10",height="1",bg="#292929",fg="#03DAC6")
    window.mainloop()
#Set the selected keys to a set of global string variables
def setbindings(f2, f3, f4, f5, root1):
    global fing2, fing3, fing4, fing5
    fing2 = f2.get()
    fing3 = f3.get()
    fing4 = f4.get()
    fing5 = f5.get()
    root1.destroy()
#The first window which opens when the program is run
root = Tk()
root.title("Select An Application")
root.geometry('800x820')
root.config(bg="#000000")
root.resizable(False,False)
#Store 4 images in a PhotoImage variable
wasdGamesphoto = PhotoImage(file=r"D:\Academic Files\SEMESTER - 4\Python Programming\Mini Project\wasdKeys.png")
powerpointphoto=PhotoImage(file=r"D:\Academic Files\SEMESTER - 4\Python Programming\Mini Project\powerpoint.png")
vlcmediaphoto=PhotoImage(file=r"D:\Academic Files\SEMESTER - 4\Python Programming\Mini Project\vlcmedia.png")
keymappingphoto=PhotoImage(file=r"D:\Academic Files\SEMESTER - 4\Python Programming\Mini Project\keymapping.png")
teamname=PhotoImage(file=r"D:\Academic Files\SEMESTER - 4\Python Programming\Mini Project\TeamLabel.png")
teamName=Label(root,image=teamname,background="#000000").place(x=60,y=10)
#Title Label
title=Label(root, text="SELECT APPLICATION", font="Helvetica 25 bold italic", fg="#FFFFFF",background="#000000").place(x=150,y=135)

#Create 4 buttons indicating the applications, these buttons will have the above images instead of text
wasdGame=Button(root,command=wasdMapping,image=wasdGamesphoto,background="#000000").place(x=60,y=215)
powerpoint=Button(root,command=powerpointMapping,image=powerpointphoto,background="#000000").place(x=430,y=195)
keymapping=Button(root,command=customMapping,image=keymappingphoto,background="#000000").place(x=60,y=545)
vlcmedia=Button(root,command=vlcmediaMapping,image=vlcmediaphoto,background="#000000").place(x=433,y=505)
root.mainloop()
#Print the keys selected
print(fing2,fing3,fing4,fing5)
#Run only if we have every key
if fing2!='' and fing3!='' and fing4!='' and fing5!='': 
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        # read image
        ret, img = cap.read()
        img=cv2.flip(img,2)

        #We will detect hand from a specified rectangle/sub-window of the size mentioned
        cv2.rectangle(img, (300,300), (100,100), (0,255,0),0)
        #The image from the rectangle is now stored in crop_img
        crop_img = img[100:300, 100:300]

        # convert the cropped or captured hand image to grayscale, for better hand detection to identify contours
        greyImage = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

        # applying gaussian blur typically used to remove image noise and smooth it out
        #Take a square of side length 35px and blur it
        blurred = cv2.GaussianBlur(greyImage, (35, 35), 0)

        # thresholding using Otsu's Binarization method
        _, thresh1 = cv2.threshold(blurred, 127, 255,
                                cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        # Create a window displaying the threshold image
        #Set title as threahold image
        cv2.imshow('Threshold Image', thresh1)

        # Find the cv2 version installed on the system
        (version, _, _) = cv2.__version__.split('.')

        #This version is used to avoid any unpacking error
        if version == '3':
            image, contours, hierarchy = cv2.findContours(thresh1.copy(), \
                cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        #Ours is 4, we will use a copy of threshold image just so originaln threshold image is not disturbed
        elif version == '4':
            contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
                cv2.CHAIN_APPROX_NONE)

        #We will find the object with maximum foreground area, i.e. hands
        cnt = max(contours, key = lambda x: cv2.contourArea(x))

        #Create one more rectangle around the contour
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(crop_img, (x, y), (x+w, y+h), (0, 0, 255), 0)

        # Find convex hull from the contours
        hull = cv2.convexHull(cnt)

        # Draw contours
        drawing = np.zeros(crop_img.shape,np.uint8)
        cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 0)
        cv2.drawContours(drawing, [hull], 0,(0, 0, 255), 0)

        # Find convex hull
        hull = cv2.convexHull(cnt, returnPoints=False)

        # Finding convexity defects
        defects = cv2.convexityDefects(cnt, hull)
        count_defects = 0
        cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)

        # Apply Cosine Rule to find angle for all defects i.e. hulls between the fingers with angle > 90 degrees and ignore defects
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]

            #We then find the far, end and start region of the contour
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])

            # Find length of all sides of triangle
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

            # apply cosine rule here
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

            # ignore angles < 90 and highlight rest with white dots
            if angle <= 90:
                count_defects += 1
                cv2.circle(crop_img, far, 1, [0,0,0], -1)
            #dist = cv2.pointPolygonTest(cnt,far,True)

            # draw a line from start to end i.e. the convex points (finger tips)
            cv2.line(crop_img,start, end, [0,255,0], 2)
            #cv2.circle(crop_img,far,5,[0,0,255],-1)

        #Add your functions here
        #If two finger is detected i.e. one defect/hull
        if count_defects == 1:
            cv2.putText(img,"2 fingers", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
            p.press(fing2)
        #If three fingers are detected i.e. two defects/hulls
        elif count_defects == 2:
            cv2.putText(img, "3 fingers", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
            p.press(fing3)
        #If four fingers are detected i.e. three defects/hulls
        elif count_defects == 3:
            cv2.putText(img,"4 fingers", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
            p.press(fing4)
        #If five fingers are detected i.e. four defects/hulls
        elif count_defects == 4:
            cv2.putText(img,"5 fingers", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
            p.press(fing5)
        #No hulls then that means no fingers or one finger
        elif count_defects==0:
            cv2.putText(img,"1 or No fingers", (5, 50),cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

        #Show the contours bw image and also the cropped image
        cv2.imshow('Gesture', img)
        all_img = np.hstack((drawing, crop_img))
        cv2.imshow('Contours', all_img)

        #Read images every 10ms / check is any key is pressed every 10ms
        k = cv2.waitKey(10)
        #If ESC key is pressed
        if k == 27:
            break