from django.conf.urls import url
from certificate_request import views
urlpatterns = [
    url('req/(?P<idd>\w+)',views.req),
    url('reject/(?P<idd>\w+)',views.reject),
    url('admin/(?P<idd>\w+)',views.rejectadmin),
    url('send/(?P<idd>\w+)',views.send),
    url('for/(?P<idd>\w+)', views.recom),

    url('view/',views.view),
    url('viewfaculty/',views.viewfaculty),
    url('viewstatus/',views.viewstatus),
    url('va/',views.va),
    url('vr/',views.vr),
    url('reason/(?P<idd>\w+)',views.vrs),
    url('public/',views.public),

]

