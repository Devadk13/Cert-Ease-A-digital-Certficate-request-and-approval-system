from django.shortcuts import render
from certificate.models import Certificate
from django.db.models import Q

# Create your views here.
def cer(request):
    am=''


    if request.method=='POST':
        nm=request.POST.get('name')
        obv=Certificate.objects.filter(Q(name=nm))
        if(len(obv)>0):
            am='user'
        else:
            obj=Certificate()
            obj.name=request.POST.get('name')
            obj.save()
            am='m'
    context={
            'msg':am,
        }

    return render(request,'certificate/certificate.html',context)


def view(request):
    obj=Certificate.objects.all()
    context={
        'a':obj
    }
    return render(request,'certificate/viewcertificate.html',context)

def delcert(request):
    obj=Certificate.objects.all()
    context={
        'a':obj
    }
    return render(request,'certificate/deletecertificate.html',context)

def dele(request,idd):
    obb=Certificate.objects.get(c_id=idd).delete()
    return delcert(request)



