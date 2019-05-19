import cv2 as cv
print( cv.__version__ )

def show_webcam(mirror=False):
    cam = cv.VideoCapture(0)
    while True:
        ret_val, frame = cam.read()
        # flip video frame if mirrored
        if mirror: 
            frame = cv.flip(frame, 1)
        cv.imshow('Webcam feed', frame)
        # press esc to quit
        if cv.waitKey(1) == 27: 
            break  
    # release
    cv.destroyAllWindows() 


def main():
    show_webcam(mirror=True)

print( 'press esc to quit' )
main()

