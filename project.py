import cv2 as cv

img = cv.imread(r"C:\Users\saurav\Pictures\Camera Roll/WIN_20240324_17_26_08_Pro.jpg")
#%%
img = cv.resize(img, (640,480))

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

retval,thresh= cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV)        


gauss = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 115, 1)

retval2,otsu = cv.threshold(img_gray, 227,255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)


cv.imshow('hand',img)
cv.imshow('hand gray',img_gray)
cv.imshow('hand bin',thresh)
cv.imshow('adapative thresholding', gauss)
cv.imshow('otsu thresholding', otsu)


cv.waitKey(0)
cv.destroyAllWindows()