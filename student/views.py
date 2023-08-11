from django.http import HttpResponse
from django.shortcuts import render

from faculty.models import Faculty
from student.models import Students
from department.models import Department
from login.models import Login
from django.db.models import Q
# Create your views here.

def stud(request):
    ss=request.session["u_id"]
    obj1=Faculty.objects.get(f_id=ss)

    a1=''
    if request.method=='POST':
        p=request.POST.get('phone')
        e=request.POST.get('email')
        obv=Students.objects.filter(Q(contact_no=p) | Q(email_id=e) | Q(contact_no=p) & Q(email_id=e))
        if len(obv)>0:
            print('user')
            a1='user'
        else:
            obj=Students()
            obj.name=request.POST.get('name')
            obj.d_id=obj1.d_id
            obj.address=request.POST.get('address')
            obj.batch=request.POST.get('batch')
            obj.contact_no=request.POST.get('phone')
            obj.email_id=request.POST.get('email')
            obj.year=request.POST.get('year')
            obj.password=request.POST.get('password')
            obj.f_id=ss
            obj.save()

            ob=Login()
            ob.username=obj.email_id
            ob.password=obj.password
            ob.u_id=obj.student_id
            ob.type='student'
            ob.save()
            a1='ss'
    context = {
        'y': obj1,
        'msg':a1
    }
    return render(request,'student/student.html',context)


def chp(request):
    al=''
    bl=''
    if request.method == 'POST':
        ss = request.session.get("u_id")
        current_password = request.POST.get('pass1')
        new_password = request.POST.get('pass')

        try:
            user = Login.objects.get(u_id=ss, password=current_password, type='student')
        except Login.DoesNotExist:
            bl='g'
            cont={
                'mg':bl,
            }
            return render(request,'student/changepass.html',cont)

        user.password = new_password
        user.save()
        al='m'
        context={
            'msg':al,
        }


        return render(request,'student/changepass.html',context)

    return render(request,'student/changepass.html')





