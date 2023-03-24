
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from AnimalsBack import settings
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/animal/', include('Animal.urls')),
    re_path(r'assets/(?P<path>.*)$',serve,{'document_root': settings.MEDIA_ROOT}),
]