# authentication/middleware.py

from django.conf import settings
from django.contrib.auth import logout
from django.utils.timezone import now
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime

class AutoLogoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Si el usuario no está autenticado, no hacer nada y retornar
        if not request.user.is_authenticated:
            return

        # Obtener el tiempo actual
        current_time = now()
        # Obtener la última actividad de la sesión
        last_activity = request.session.get('last_activity')

        # Si hay una última actividad registrada
        if last_activity:
            last_activity = datetime.fromisoformat(last_activity)
            # Calcular el tiempo transcurrido desde la última actividad
            elapsed_time = (current_time - last_activity).total_seconds()
            # Si el tiempo transcurrido es mayor que el tiempo de expiración de la sesión+
            if elapsed_time > settings.SESSION_COOKIE_AGE:
                # Cerrar sesión del usuario
                logout(request)
                # Limpiar la sesión
                request.session.flush()
                return

        # Actualizar la última actividad de la sesión con el tiempo actual
        request.session['last_activity'] = current_time.isoformat()
