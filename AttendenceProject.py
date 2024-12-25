import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'ImagesBasic'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
#Searches myList and adds each image to images array
# does the same with classNames array
#Loading Images
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        #Step 1: Converting to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #Step 2: Encoding Image
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    
    return encodeList

def markAttendence(name):
    with open('Attendence.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\r{name}, {dtString}')

encodeListKnown = findEncodings(images)
print('Encoding Complete')



#Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
    #cv2.imshow('Webcam Feed', img)
    #Step 3: Find matches between encodings
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #print(faceDis)
        #Finding lowest number (greatest match) in faceDis Array
        matchIndex = np.argmin(faceDis)

        #Returns name of best match image
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            
            #print(name)
            #puting rectangle around image
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4 #Scaled down img to 1/4 size above
            cv2.rectangle(img, (x1,y1), (x2, y2), (0,255,0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0,255,0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 255, 255),3)
            markAttendence(name)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting webcam feed...")
        break
    

# faceLoc = face_recognition.face_locations(imgElon)[0]
# encodeElon = face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255), 2)

# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255,0,255), 2)

# #if(encodeElon.all() == encodeTest.all()): print(True)
# #else: print(False)
# results = face_recognition.compare_faces([encodeElon], encodeTest)
# faceDis = face_recognition.face_distance([encodeElon], encodeTest)