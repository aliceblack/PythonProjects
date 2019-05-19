from tello import Tello
import cv2 as cv

#Capture stream using OpenCV
def videoCapture():
    return cv.VideoCapture('udp://@0.0.0.0:11111')

#Initialize drone
tello = Tello()

def command():
    tello.send_command('command')

def streamOn():
    tello.send_command('streamon')
  
def takeoff():
    tello.send_command('takeoff')

def land():
    tello.send_command('land')

def forward():
    tello.send_command('forward 40')

def back():
    tello.send_command('back 40')

def couterClockwise():
    tello.send_command('ccw 45')

def clockWise():
    tello.send_command('cw 45')

def up():
    tello.send_command('up 40')

def down():
    tello.send_command('down 40')

def left():
    tello.send_command('left 40')

def right():
    tello.send_command('right 40')
 
def flipForward():
    tello.send_command('flip f')

def flipBack():
    tello.send_command('flip b')

def flipLeft():
    tello.send_command('flip l')

def flipRight():
    tello.send_command('flip r')