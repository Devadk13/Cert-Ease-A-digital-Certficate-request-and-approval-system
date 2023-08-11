from django.conf.urls import url
from certificate import views

urlpatterns=[
    url('add/',views.cer),
    url('view/',views.view),
    url('del/',views.delcert),
    url('d/(?P<idd>\w+)', views.dele),
]


