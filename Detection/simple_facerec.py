import face_recognition
import cv2
import os
import glob
import numpy as np
from .crud import AddConnection
class SimpleFacerec:
    def __init__(self,module):
        #paramettre de class (image encoder + leur nom)
        self.known_face_encodings = []
        self.known_face_names = []
        self.module = module
        # recadrage de l'image pour augementer le nombre de ips
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Chargement des images à encoder
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} Nombre d'image trouver est de .".format(len(images_path)))

        #Stockage des images encoder et leur nom
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Récupération du nom de l'image (en splitant le path de l'extention
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Encodage de l'image
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # sauvgarde du nom et de l'image dans notre objet
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Encodage des images charger ...")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Detecter les visages appercu par la caméra et les encoder
        # Convertion des image de BGR color (utiliser par OpenCV ) a RGB color (utilisé par face_recognition)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        #Detection de la localisation de l'image via face_location qui detect automatiquement les visages et ainsi faire l'encodage
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            #Vérifier si le visage existe dans la base d'image encoder
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Inconnu"

            # # si un match est found dans known_face_encodings,je prend la premier.
            # si True dans matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # sinon, je retourne le premier visage connu avec le score de similarité(distance le plus proche)
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
                AddConnection(self.module, name)
            face_names.append(name)

        # conversion a un numpy array pour ajuste les coordonnée avec la frame opencv
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names
