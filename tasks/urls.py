from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tasks.views import TaskView, RegisterUser  # Import RegisterUser here

# Set up the router
router = routers.DefaultRouter()
router.register(r'tasks', TaskView, 'task')

# URL patterns
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', include_docs_urls(title='Tasks API')),
    path('api/v1/register/', RegisterUser.as_view(), name='register_user'),  # Make sure RegisterUser is imported
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
