from skimage.measure import compare_ssim
import argparse
import imutils
from cv2 import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f","--first",required=True,help="First input image")
ap.add_argument("-s","--second", required=True,help="second")
args=vars(ap.parse_args())

imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])

grayA=cv2.cvtColor(imageA,cv2.COLOR_BGR2GRAY)
grayB=cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)

(score, diff) = compare_ssim(grayA,grayB, full=True)
diff = (diff*255).astype("uint8")
print("SSIM: {}".format(score))

thresh = cv2.threshold(diff,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    (x,y,w,h) = cv2.boundingRect(c)
    cv2.rectangle(imageA, (x,y), (x+w,y+h), (0,0,255), 2)
    cv2.rectangle(imageB, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imshow('grayA',imageA)
cv2.imshow('grayB',imageB)
cv2.imshow('Diff',diff)
cv2.imshow('thresh',thresh)

cv2.waitKey(0)