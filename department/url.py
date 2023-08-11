from django.conf.urls import url
from department import views

urlpatterns = [
    url('dep/', views.dep),
    url('dp/',views.deldep),
    url('for/(?P<idd>\w+)',views.dele),


]

