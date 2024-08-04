"""
URL configuration for clase_DRF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api_rest.views import AlumnoView, AlumnoCreateView, OnlyAlumno, AlumnoUpdateView, AlumnoDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumno/<pk>/', OnlyAlumno.as_view(), name='alumno-listar'),
    path('alumnos/', AlumnoView.as_view(), name='alumnos-listar'),
    path('alumno/add/', AlumnoCreateView.as_view(), name='alumno-crear'),
    path('alumno/update/<pk>/', AlumnoUpdateView.as_view(), name='alumno-actualizar'),
    path('alumno/delete/<pk>/', AlumnoDeleteView.as_view(), name='alumno-eliminar'),
]
