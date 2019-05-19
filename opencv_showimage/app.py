import cv2
print( cv2.__version__ )

imageName = "cygnus.jpg" 

image = cv2.imread( imageName, cv2.IMREAD_COLOR )
cv2.imshow('Showing image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
