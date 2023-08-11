from django.shortcuts import render
from department.models import Department
from django.db.models import Q
# Create your views here.

def dep(request):
    al=''
    if request.method=='POST':
        d=request.POST.get('Deptname')

        obv=Department.objects.filter(Q(name=d))
        if(len(obv)>0):
            al='user'
        else:
            obj=Department()
            obj.name=request.POST.get('Deptname')
            obj.save()
            al='m'

    context={
            'msg': al,
        }
    return render(request, 'department/department.html',context)

def deldep(request):
    obj=Department.objects.all()
    context={
        'a':obj
    }
    return render(request, 'department/deletedep.html',context)

def dele(request,idd):
    obj=Department.objects.get(d_id=idd).delete()
    return deldep(request)






