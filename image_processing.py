import cv2
img=cv2.imread('Monalisa.jpg') #write your image name or path

#prepareatio for CLAHE
clahe=cv2.createCLAHE()
#conversion in black and white image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#apply enhancement
enh_img=clahe.apply(gray_img)
#save it to a file
cv2.imwrite('enhanced.png',enh_img)
print('Done Enhancement')



