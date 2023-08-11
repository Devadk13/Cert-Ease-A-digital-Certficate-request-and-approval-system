from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from certificate_request.models import Request
import datetime
from certificate.models import Certificate
from student.models import Students
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def reject(request,idd):
    if request.method=='POST':
        obj=Request.objects.get(r_id=idd)
        obj.reject_reason=request.POST.get('message')
        obj.status='rejected'
        obj.save()
        return viewfaculty(request)
    return render(request, 'certificate_request/rejectmessage.html')



def recom(request,idd):
    obb=Request.objects.get(r_id=idd)
    obb.status='Forwarded'
    obb.save()
    return viewfaculty(request)


def rejectadmin(request,idd):
    if request.method=='POST':
        obj=Request.objects.get(r_id=idd)
        obj.reject_reason=request.POST.get('reply')
        obj.status='admin_rejected'
        obj.save()
        return HttpResponseRedirect('/crequest/view/#p')
    return render(request, 'certificate_request/rejectmessageadmin.html')


def req(request,idd):
    ss=request.session["u_id"]
    obv=Students.objects.get(student_id=ss)
    obb=Certificate.objects.get(c_id=idd)
    context={
        'kk':obb
    }
    if request.method=='POST':
        obj=Request()
        obj.need=request.POST.get('need')
        obj.c_id=idd
        obj.f_id=obv.f_id
        obj.student_id=ss
        obj.date=datetime.datetime.today()
        obj.status="Pending"
        obj.uploaded_documents="no documents"
        obj.save()

        # subject="Certificate Request"
        # message="Test email"
        # from_email=settings.EMAIL_HOST_USER
        # recipient_list=["sunilkumarsk266@gmail.com"]
        # send_mail(subject,message,from_email,recipient_list)
        return HttpResponseRedirect('/cert/view/#s')
    return render(request, 'certificate_request/requestcertificate.html',context)

def send(request,idd):
    if request.method=='POST':
        obj=Request.objects.get(r_id=idd)
        myfile=request.FILES['file']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.uploaded_documents=myfile.name
        obj.status = "Issued"
        obj.save()
        return HttpResponseRedirect('/crequest/view/#p')
    return render(request, 'certificate_request/senddocument.html')


def view(request):
    obj=Request.objects.filter(status='Forwarded')
    context={
        'kk':obj
    }
    return render(request,'certificate_request/viewradmin.html',context)

def viewfaculty(request):
    ss=request.session["u_id"]
    obj=Request.objects.filter(f_id=ss,status='Pending')
    context={
        'b':obj
    }
    return render(request,'certificate_request/viewrfaculty.html',context)

def viewstatus(request):
    ss=request.session["u_id"]
    obj=Request.objects.filter(student_id=ss)
    context={
        'c':obj

    }
    return render(request,'certificate_request/viewstatus.html',context)

def va(request):
    obj=Request.objects.filter(status="Issued")
    context={
        'c':obj
    }
    return render(request,'certificate_request/viewapproved.html',context)

def vr(request):
    obj=Request.objects.filter(status="admin_rejected")
    context={
        'c':obj
    }
    return render(request,'certificate_request/viewrejected.html',context)


def vrs(request,idd):
    ob=Request.objects.get(r_id=idd)
    context={
        'kk':ob
    }
    return render(request,'certificate_request/viewreason.html',context)

def public(request):
    obj=''
    if request.method=='POST':
        s=request.POST.get('s')
        obj=Request.objects.filter(r_id=s,status='Issued')
        if len(obj)<1:
            obj=''
        else:
            obj=Request.objects.get(r_id=s,status='Issued')
    context={
        'kk':obj
    }
    return render(request,'certificate_request/public.html',context)




