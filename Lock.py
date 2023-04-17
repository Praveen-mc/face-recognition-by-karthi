import face_recognition as fr
import pickle
import cv2
import os
cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
capture = cv2.VideoCapture(0) #capturing video

video_capture = cv2.VideoCapture(0)
face_is_match = False
face_encodings = []
known_face_encodings = pickle.load(open('C:\\Users\\Admin\\Documents\\face_lock\\face_db\\encode.pickle','rb'))
      
while True:
        ret, frame = video_capture.read()
        face_locations = fr.face_locations(frame, model="hog")
        face_encodings = fr.face_encodings(frame, face_locations)
               
        face_names = []
        name = "Unknown"

        for face_encoding in face_encodings:
                matches = fr.compare_faces(known_face_encodings, face_encoding, 0.4)
                                                                                                                
                #find first match
                if True in matches:
                        first_known_face = matches.index(True)
                        file=open("C:YourFile.txt","r")
                        print(file.read())
                        face_is_match = True
                
                else:
                        print("Access Denied")


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
                # cv2.rectangle(image ,start_point, end_point, color, thickness)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                # cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
                cv2.putText(frame, 'FACE',(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,2),1,cv2.LINE_AA)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

                capture.release()
                cv2.destroyAllWindows()
