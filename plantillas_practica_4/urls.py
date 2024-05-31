
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("presentacion/",views.presentacion,name="presentacion"),
    path("fotos/",views.fotos,name="fotos"),
]
