from django.shortcuts import render
from faculty.models import Faculty
from department.models import Department
# Create your views here.
from login.models import Login
from django.db.models import Q

def faculty(request):
    al=''
    obj1 = Department.objects.all()
    if request.method=='POST':
        ph=request.POST.get('phone')
        e=request.POST.get('email')
        obv=Faculty.objects.filter(Q(contact_no=ph) | Q(email_id=e) | Q(contact_no=ph) & Q(email_id=e))
        if len(obv)>0:
            print('user')
            al='user'
        else:
            obj=Faculty()
            obj.name=request.POST.get('name')
            obj.d_id=request.POST.get('dp')
            obj.contact_no=request.POST.get('phone')
            obj.email_id=request.POST.get('email')
            obj.password=request.POST.get('password')
            obj.save()

            ob = Login()
            ob.username = obj.email_id
            ob.password = obj.password
            ob.u_id = obj.f_id
            ob.type = 'faculty'
            ob.save()
            al='ss'
    context = {
        'x': obj1,
        'msg':al,
    }
    return render(request,'faculty/faculty.html',context)

def m(request):
    return render(request, 'faculty/viewstudent.html')



