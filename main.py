from PIL import Image, Image, ImageEnhance, ImageOps

import cv2


outputWidth = 3000
outputHeight = 2100


PilImg = Image.open("Image.jpg")
PilImg.save("Temp.jpg", dpi=(320,320))

orgImg = cv2.imread("Temp.jpg")
grayImage = cv2.cvtColor(orgImg,cv2.COLOR_BGR2GRAY)
resizedImage = cv2.resize(grayImage,(outputWidth,outputHeight),cv2.INTER_AREA)
cv2.imwrite("Temp2.tif", grayImage)
cv2.imwrite("Temp3.tif", resizedImage)
h, w = grayImage.shape

PilImage2 = Image.fromarray(resizedImage)

PilImage2.save("result.tif", dpi=(320,320), compression='LZW')






cv2.imshow('Gray image', grayImage)
cv2.imshow('resized image', resizedImage)



cv2.waitKey(0)
cv2.destroyAllWindows()