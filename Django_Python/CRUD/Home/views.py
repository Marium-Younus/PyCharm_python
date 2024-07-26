from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import EmpTbl

def func_home(request):
    return render(request,"index.html")

def func_show(request):
    data = EmpTbl.objects.all()
    return render(request,"show.html",{'data':data})

#-----------------------------------Insert Record
def func_save(request):
    if request.method == 'POST':
        EmpName = request.POST['fullName']
        EmpEmail = request.POST['email']
        EmpMobile = request.POST['mobile']
        EmpCity = request.POST['city']
        EmpTbl(EmpName= EmpName,EmpEmail=EmpEmail,EmpMobile=EmpMobile,EmpCity=EmpCity).save()
        msg = "Data Stored Succesfully"
        return  render(request,"index.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")
#-----------------------------------Delete Record

def func_delete(request):
    del_id=request.GET['id']
    EmpTbl.objects.filter(Empid=del_id).delete()
    return HttpResponseRedirect("showrecord")

#-----------------------------------edit Record get

def func_edit(request):
    e_id = request.GET['id']
    for data in EmpTbl.objects.filter(Empid=e_id):
        id = data.Empid
        name = data.EmpName
        email = data.EmpEmail
        mobile = data.EmpMobile
        city = data.EmpCity
    return render(request,"edit.html",{'Empid':id,'EmpName':name,'EmpEmail':email,'EmpMobile':mobile,'EmpCity':city})
#-----------------------------------update Record
def update_record(request):

    if request.method == 'POST':
        u_id = request.POST['hideid']
        n_var = request.POST['fullName']
        e_var = request.POST['email']
        m_var = request.POST['mobile']
        c_var = request.POST['city']
        EmpTbl.objects.filter(Empid=u_id).update(EmpName=n_var,
                                                 EmpEmail=e_var,
                                                 EmpMobile=m_var,
                                                 EmpCity=c_var)
        return HttpResponseRedirect("showrecord")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

