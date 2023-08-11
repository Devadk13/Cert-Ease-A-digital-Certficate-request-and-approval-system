from django.shortcuts import render
from django.http import HttpResponseRedirect
from login.models import Login
# Create your views here.

def login(request):
    if request.method =="POST":
        uname = request.POST.get("name")
        password=request.POST.get("pass")
        obj=Login.objects.filter(username=uname,password=password)
        tp=""

        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "admin":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp =="student":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/student/')
            elif tp == "faculty":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/faculty/')
        else:
            objlist = "ss"
            context = {
                'msg':objlist,
            }
        return render(request,'login/login.html',context)
    return render(request,'login/login.html')


