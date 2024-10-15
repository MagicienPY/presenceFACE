from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from myapp.views import index,image_request,listEtudiant,LDW,LDW_start,TIW_start,TIW,TEI,TEI_start
urlpatterns = [
    path('',index,name="home"),
    path('upload/',image_request,name="upload"),
    path('list/',listEtudiant,name="list"),
    path('LDW',LDW,name="LDW"),
    path('LDW_start',LDW_start,name="LDW_start"),
    path('TIW',TIW,name="TIW"),
    path('TIW_start',TIW_start,name="TIW_start"),
    path('TEI',TEI,name="TEI"),
    path('TEI_start',TEI_start,name="TEI_start"),
    path('admin/', admin.site.urls)


]
if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
