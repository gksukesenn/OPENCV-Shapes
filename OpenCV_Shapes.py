import cv2
import numpy as np

img = np.zeros((512,512))
print(img.shape)#img in boyutlarýný anlamak için ekrana yazdýrdýk.
img = np.zeros((512,512,3),np.uint8)#renk özelliði eklemek için 3 boyutlu olsun dedik.
#np.uint8 bellek tasarrufu saðlar. Bi yandan da 0 ile 255 arasýnda renk kodlarý olduðundan iþaretsiz int kullanmýþ olduk.Çünkü uint zaten 0-255 arasýnda

#img[:] =255,0,0 sadece : tüm resmi kapsar.

img[200:300,100:300] =255,0,0

cv2.line(img,(0,0),(300,300),(0,255,0),3)##0.0 dan baþlayýp 300.300 e giden bir çizgi çektik yeþil renkte
#cv2.line(img,(0,0),img.shape[1],img.shape[0],(0,255,0),3)#tüm resmin köþegenini alan line


cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)#,cv2.FILLED] Eklersek tüm kareyi boyar
 
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"OPEN CV ",(300,120),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
cv2.imshow("Image",img)

cv2.waitKey(0)


