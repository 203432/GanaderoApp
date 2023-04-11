
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from AnimalsBack import settings
from rest_framework import generics
from Register.serializers import UserSerializer 
from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/animal/', include('Animal.urls')),
    path('api/v1/login/', include('Login.urls')),
    path('api/v1/register/', generics.CreateAPIView.as_view(
        serializer_class=UserSerializer,
        permission_classes=[AllowAny], # Aquí utilizamos AllowAny para permitir el registro sin autenticación
    )),
    re_path(r'assets/(?P<path>.*)$',serve,{'document_root': settings.MEDIA_ROOT}),
]