import cv2 as cv
print( cv.__version__ )


img1 = cv.imread('blend1.png')
img2 = cv.imread('blend2.png')

#Blend two images
dst = cv.addWeighted(img1,0.5,img2,0.5,0)

#Show result
cv.imshow('Image blending',dst)
#Close preview
cv.waitKey(0)
cv.destroyAllWindows()