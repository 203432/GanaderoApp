from django.urls import re_path


from Animal.views import AnimalList, AnimalDetail, AnimalListByOwner


urlpatterns = [
    re_path(r'$',AnimalList.as_view()),
    re_path(r'(?P<pk>\d+)$', AnimalDetail.as_view()),
    re_path(r'by_owner/(?P<owner_id>\d+)$', AnimalListByOwner.as_view()),
]