from rest_framework import generics
from .models import Alumno
from .serializers.alumno_serializer import AlumnoSerializer, AlumnoCreateSerializer, AlumnoUpdateSerializer

# creamos una vista para listar datos a travez del metodo GET
class AlumnoView(generics.ListAPIView):
    """
    Este endpoint lista a todos los estudiantes ingresados a la base de datos.
    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    
# creamos una vista para listar datos de un solo alumno por "id" a travez del metodo GET
class OnlyAlumno(generics.RetrieveAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

# creamos una vista para crear datos a travez del metodo POST
class AlumnoCreateView(generics.CreateAPIView):
    """
    Este endpoint sirve para o añadir a un nuevo estudiante por:
    nombre, apellidos, correo y curso.
    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoCreateSerializer

# creamos una vista para actualizar datos de un alumno por "id" a travez del metodo PUT
class AlumnoUpdateView(generics.UpdateAPIView):
    """
    Este endpoint sirve actualizar a un estudiante por:
    correo y curso.
    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoUpdateSerializer

# creamos una vista para eliminar datos de un alumno por "id" a travez del metodo DELETE
class AlumnoDeleteView(generics.DestroyAPIView):
    """
    Este endpoint sirve eliminar a un estudiante por 'id'.
    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoUpdateSerializer