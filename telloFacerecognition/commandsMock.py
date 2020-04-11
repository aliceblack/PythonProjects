import cv2 as cv

#Capture webcam stream using OpenCV
def videoCapture():
    return cv.VideoCapture(0)


def command():
    print('command')

def streamOn():
    print('streamon')
  
def takeoff():
    print('takeoff')

def land():
    print('land')

def forward():
    print('forward 40')

def back():
    print('back 40')

def couterClockwise():
    print('ccw 45')

def clockWise():
    print('cw 45')

def up():
    print('up 40')

def down():
    print('down 40')

def left():
    print('left 40')

def right():
    print('right 40')
 
def flipForward():
    print('flip f')

def flipBack():
    print('flip b')

def flipLeft():
    print('flip l')

def flipRight():
    print('flip r')