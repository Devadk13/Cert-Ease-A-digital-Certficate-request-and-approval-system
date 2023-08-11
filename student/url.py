from django.conf.urls import url
from student import views

urlpatterns = [
    url('stud/', views.stud),
    url('chp/',views.chp),


]

