from django.conf.urls import url
from faculty import views

urlpatterns = [
    url('faculty/',views.faculty),
    url('m/',views.m),

]