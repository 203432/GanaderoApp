import re
from xml.dom.minidom import Document
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from AnimalsBack import settings

from Animal.views import AnimalList


urlpatterns = [
    re_path(r'$',AnimalList.as_view()),
    # re_path(r'(?P<pk>\d+)$', TablaProfileDetail.as_view())
]