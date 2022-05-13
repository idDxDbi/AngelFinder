import cv2
import math

path = "test.png"
img = cv2.imread(path)
pointsList = []
# 获取鼠标的点
def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        print(size)
        if size != 0 and size % 3 != 0:
            cv2.line(img,tuple(pointsList[round((size-1)/3)*3]),(x,y),(0,0,255),2)
            # print(round((size-1)/3)*3)
        cv2.circle(img, (x,y),5,(0,0,255),cv2.FILLED)
        pointsList.append([x,y])
        print(pointsList)
        # print(x, y)




#求两点连成的直线斜率（梯度）
def gradient(pts1, pts2):
    return (pts2[1]-pts1[1])/(pts2[0]-pts1[0])

def getAngel(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    # print(pt1, pt2, pt3)
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt1, pt3)
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = round(math.degrees(angR))
    # print(abs(angD))

    cv2.putText(img, str(abs(angD)), (pt1[0]-40,pt1[1]-20), cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,255),2)



while True:


    if len(pointsList) % 3 == 0 and len(pointsList) != 0:
        getAngel(pointsList)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList = []
        img = cv2.imread(path)
