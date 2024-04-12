from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.urls import path

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer for obtaining a pair of access and refresh tokens with added custom claims.
    """
    @classmethod
    def get_token(cls, user):
        """
        Overrides the default method to add custom claims to the token.
        """
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    """
    View that provides a mechanism for obtaining a JWT token pair.
    """
    serializer_class = MyTokenObtainPairSerializer

# urls.py in your tasks app
urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Add other URL configurations as needed
]
