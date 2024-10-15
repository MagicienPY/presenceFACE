from datetime import datetime

from django.shortcuts import render
import pyrebase
from Detection.Detection import run
from .forms import PickForm
from .models import UploadImage

firebaseConfig = {
  "apiKey": "AIzaSyDyJMu-E_n3bN7-pQEXP6C2J1BpILOO1ec",
  "authDomain": "detection-423c7.firebaseapp.com",
  "databaseURL": "https://detection-423c7-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "detection-423c7",
  "storageBucket": "detection-423c7.appspot.com",
  "messagingSenderId": "485699384375",
  "appId": "1:485699384375:web:c1b5996d67dbc0c8137bb2",
  "measurementId": "G-3WNXEZPC7L"
};

firebase = pyrebase.initialize_app(firebaseConfig)
database=firebase.database()

def index(request):

    return render(request, 'myapp/index.html')


def image_request(request):
    if request.method == 'POST':
        form = PickForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Getting the current instance object to display in the template
            img_object = form.instance

            return render(request, 'myapp/upload_picture.html', {'form': form, 'img_obj': img_object})
    else:
        form = PickForm()

    return render(request, 'myapp/upload_picture.html', {'form': form})

def listEtudiant(request,):
    etudiants = UploadImage.objects.all();
    return render(request,'myapp/list_etudiant.html',context={'etudiants':etudiants})

def LDW(request):
    etudiants = UploadImage.objects.all();
    now = datetime.now()
    context = {
        'etudiants': etudiants,
        'name': "",
        'date': now.strftime("%m/%d/%Y"),
    }

    result = database.child('LDW').child(now.strftime("%m:%d:%Y")).shallow().get().val()
    if result is not None:
        list_time=[]
        for i in result:
            list_time.append(i)
        names = []
        for i in list_time:
            names.append( database.child('LDW').child(now.strftime("%m:%d:%Y")).child(i).get().val())
        etudiants = UploadImage.objects.all();

        context = {
            'etudiants':etudiants,
            'name': names,
            'date': now.strftime("%m/%d/%Y"),
        }
        return render(request, 'myapp/LDW.html', context)
    context = {
        'etudiants': etudiants,
        'name': "",
        'date': now.strftime("%m/%d/%Y"),
    }
    return render(request, 'myapp/LDW.html', context)

def LDW_start(request):
    run("LDW")
    return render(request, 'myapp/LDW.html')
def TIW(request):
    etudiants = UploadImage.objects.all();
    now = datetime.now()
    context = {
        'etudiants': etudiants,
        'name': "",
        'date': now.strftime("%m/%d/%Y"),
    }
    now = datetime.now()
    result = database.child('TIW').child(now.strftime("%m:%d:%Y")).shallow().get().val()
    if result is not None:
        list_time=[]
        for i in result:
            list_time.append(i)
        names = []
        for i in list_time:
            names.append( database.child('TIW').child(now.strftime("%m:%d:%Y")).child(i).get().val())
        etudiants = UploadImage.objects.all();
        print(names)
        context = {
            'etudiants': etudiants,
            'name': names,
            'date': now.strftime("%m/%d/%Y"),
        }

        return render(request, 'myapp/TIW.html', context)
    context = {
        'etudiants': etudiants,
        'name': "",
        'date': now.strftime("%m/%d/%Y"),
    }
    return render(request, 'myapp/TIW.html', context)

def TIW_start(request):
    run("TIW")
    return render(request, 'myapp/TIW.html')

def TEI(request):
    etudiants = UploadImage.objects.all();
    now = datetime.now()
    result = database.child('TEI').child(now.strftime("%m:%d:%Y")).shallow().get().val()
    context = {
        'etudiants': etudiants,
        'name': "",
        'date': now.strftime("%m/%d/%Y"),
    }

    if result is not None:
        list_time=[]
        for i in result:
            list_time.append(i)
        names = []
        for i in list_time:
            names.append( database.child('TEI').child(now.strftime("%m:%d:%Y")).child(i).get().val())

        etudiants = UploadImage.objects.all();

        context = {
            'etudiants': etudiants,
            'name': names,
            'date': now.strftime("%m/%d/%Y"),
        }
        return render(request, 'myapp/TEI.html', context)
    return render(request, 'myapp/TEI.html', context)

def TEI_start(request):
    run("TEI")

    return render(request, 'myapp/TEI.html')

