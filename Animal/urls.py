from django.urls import re_path


from Animal.views import AnimalList, AnimalDetail


urlpatterns = [
    re_path(r'$',AnimalList.as_view()),
    re_path(r'(?P<pk>\d+)$', AnimalDetail.as_view())
]