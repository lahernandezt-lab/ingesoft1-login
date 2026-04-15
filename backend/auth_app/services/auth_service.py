import hashlib
from auth_app.repositories.user_repository import UserRepository


class AuthService:

    @staticmethod
    def hash_password(password):
        password_bytes = password.encode('utf-8')
        hash_object = hashlib.sha512(password_bytes)
        password_hash = hash_object.hexdigest()
        return password_hash

    @staticmethod
    def authenticate(correo, password):

        # 1. Buscar el usuario usando el repositorio
        repo = UserRepository()
        user = repo.find_by_correo(correo)

        # 2. Si no existe, error
        if not user:
            return {
                "success": False,
                "message": "Usuario no encontrado"
            }

        # 3. Aplicar hash al password recibido para comparar
        input_password_hash = AuthService.hash_password(password)

        # 4. Comparar con el hash almacenado en la base de datos
        if input_password_hash != user.password_hash:
            return {
                "success": False,
                "message": "Contraseña incorrecta"
            }

        # 5. Si todo coincide, éxito
        return {
            "success": True,
            "secret_phrase": user.secret_phrase
        }
