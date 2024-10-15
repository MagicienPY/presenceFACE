import datetime

import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyDyJMu-E_n3bN7-pQEXP6C2J1BpILOO1ec",
  'authDomain': "detection-423c7.firebaseapp.com",
  'databaseURL': "https://detection-423c7-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "detection-423c7",
  'storageBucket': "detection-423c7.appspot.com",
  'messagingSenderId': "485699384375",
  'appId': "1:485699384375:web:c1b5996d67dbc0c8137bb2",
  'measurementId': "G-3WNXEZPC7L"
};

firebase = pyrebase.initialize_app(firebaseConfig)
database=firebase.database()
now = datetime.datetime.now()

print(now.strftime("%m:%d:%Y"))
#create

def AddConnection(module,name):
    date = now.strftime("%m:%d:%Y")
    data = {"name":name,"date":now.strftime("%m/%d/%Y")}
    database.child(module).child(date).child(name).set(data)
