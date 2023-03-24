from django.urls import re_path


from Register.views import RegisterAPI


urlpatterns = [
    re_path(r'$',RegisterAPI.as_view()),
    # re_path(r'(?P<pk>\d+)$', TablaProfileDetail.as_view())
]