import cv2
import numpy as np

img = np.zeros((512,512))
print(img.shape)#img in boyutlar�n� anlamak i�in ekrana yazd�rd�k.
img = np.zeros((512,512,3),np.uint8)#renk �zelli�i eklemek i�in 3 boyutlu olsun dedik.
#np.uint8 bellek tasarrufu sa�lar. Bi yandan da 0 ile 255 aras�nda renk kodlar� oldu�undan i�aretsiz int kullanm�� olduk.��nk� uint zaten 0-255 aras�nda

#img[:] =255,0,0 sadece : t�m resmi kapsar.

img[200:300,100:300] =255,0,0

cv2.line(img,(0,0),(300,300),(0,255,0),3)##0.0 dan ba�lay�p 300.300 e giden bir �izgi �ektik ye�il renkte
#cv2.line(img,(0,0),img.shape[1],img.shape[0],(0,255,0),3)#t�m resmin k��egenini alan line


cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)#,cv2.FILLED] Eklersek t�m kareyi boyar
 
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"OPEN CV ",(300,120),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
cv2.imshow("Image",img)

cv2.waitKey(0)


