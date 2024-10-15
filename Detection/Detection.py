import cv2
from .simple_facerec import SimpleFacerec
def run(name):

    #Encodage des image de la base d'image connue
    sfr = SimpleFacerec(name)
    sfr.load_encoding_images("G:\Etude\M2_Paris_8\TEI\src\media\images")

    #Chargement de la camera
    cap = cv2.VideoCapture(0)



    while True:
        #lecture de la frame
        ret,frame = cap.read()

        #Detection du visage
        face_locations,face_names = sfr.detect_known_faces(frame)
        for face_loc,name in zip(face_locations,face_names):
            #print(face_loc)
            y1,x1,y2,x2 = face_loc[0],face_loc[1],face_loc[2],face_loc[3]

            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        cv2.imshow("Frame",frame)

        key = cv2.waitKey(1)
        if key ==27:
            break

    cap.release()
    cv2.destroyAllWindows()
