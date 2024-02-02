# En views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Policia, Infraccion, Vehiculo
from .serializers import InfraccionPayloadSerializer, InfraccionSerializer


class CargarInfraccionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Validar si el token está presente
        if not request.auth:
            return Response({'error': 'Token no proporcionado'},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Obtener el oficial asociado al token
        try:
            oficial = Policia.objects. \
                get(id=request.data.get('numero_identificativo_oficial'))
        except Policia.DoesNotExist:
            return Response({'error': 'Oficial no encontrado'},
                            status=status.HTTP_404_NOT_FOUND)

        # Validar que el token pertenezca al oficial
        if request.auth.user.id != oficial.user.id:
            return Response({'error': 'Token no coincide con el \
                             oficial actual'},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Validar y deserializar el payload
        serializer = InfraccionPayloadSerializer(data=request.data)
        if serializer.is_valid():
            # Crear y guardar la infracción en la base de datos
            infraccion = Infraccion(
                placa_patente=serializer.validated_data['placa_patente'],
                timestamp=serializer.validated_data['timestamp'],
                comentarios=serializer.validated_data['comentarios'],
                oficial_id=serializer.
                validated_data['numero_identificativo_oficial'],
            )
            infraccion.save()

            return Response({'mensaje': 'Infracción registrada correctamente'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Datos de infracción inválidos'},
                            status=status.HTTP_400_BAD_REQUEST)


class ListarInfraccionesView(generics.ListAPIView):
    serializer_class = InfraccionSerializer

    def get_queryset(self):
        email_propietario = self.request.query_params. \
           get('email_propietario', None)
        queryset = Infraccion.objects.none()

        if email_propietario:
            vehiculos_propietario = Vehiculo.objects.\
               filter(propietario__correo_electronico=email_propietario)
            queryset = Infraccion.objects.\
                filter(placa_patente__in=vehiculos_propietario.
                       values_list('placa_patente', flat=True))

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            return Response({'mensaje': 'No se encontraron infracciones \
                            para el correo proporcionado'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
