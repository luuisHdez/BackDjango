 
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tasks import views

# Set up the router
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'task')

# URL patterns
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', include_docs_urls(title='Tasks API')),
# Adding Path to register module
    path('api/v1/register/', RegisterUser.as_view(), name='register_user')
]
