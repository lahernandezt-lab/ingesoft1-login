from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from auth_app.services.auth_service import AuthService


@api_view(['POST'])
def login(request):
    # 1. Extraer datos
    correo = request.data.get('correo')
    password = request.data.get('password')

    # 2. Validar campos
    if not correo or not password:
        return Response(
            {"success": False, "message": "Correo y contraseña son requeridos"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # 3. Llamar al service
    result = AuthService.authenticate(correo, password)

    # 4. Retornar respuesta según resultado
    if result["success"]:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_401_UNAUTHORIZED)
