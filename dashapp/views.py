from django.shortcuts import render,redirect
from dashapp.models import Department

# Create your views here.


def home(request):
    data=Department.objects.all()
    data = Department.objects.filter(status=True)
    context={}
    context['Departments']=data
    return render(request, 'dash.html',context)


def addDepartment(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    else:
        #  capture  form data 
        dept=request.POST["Department"]
        Disc=request.POST["Discriptions"]
        b=Department.objects.create( DepartmentName=dept, Description=Disc)
        b.save()
        return redirect('/')
    
# def Deletedepart(request, departid):
#     # Get the department object
#     depart = Depart.objects.get(dept_id=departid)
#     # Update the status to False (inactive)
#     depart.status = False
#     depart.save()  # Save the updated status to the database
#     return redirect('/')

def deleteDepartment(request,deptid):
    depart = Department.objects.get(dept_id=deptid)
    depart.status = False
    depart.save()  # Save the updated status to the database
    return redirect('/')


def updateDepartment(request,deptid):
    # b=Depart.objects.filter(id=bookid)
    d=Department.objects.get(dept_id=deptid) 
    if request.method=='GET':
        context={}
        context['Department']=d # used with GET method
        return render(request,'update.html',context)
    else:
        dt=Department.objects.filter(dept_id=deptid)
        dept=request.POST['Department']
        disc=request.POST['description']
        d=Department.objects.update( DepartmentName=dept, Description=disc)
        # dt.update(depart_name=n,description=d)
        return redirect('/')

# def updateDepartment(request,deptid):
    # if request.method == 'GET':
    #     d=Department.objects.get(id=deptid)
    #     context={}
    #     context['Department']=d
    #     return render(request, 'update.html',context)
    # else:
    #     #  capture  form data
    #     d=Department.objects.filter(id=deptid)
    #     deptid=request.POST["dept_id"]
    #     dept=request.POST["Department"]
    #     Disc=request.POST["Discriptions"]
    #     d=Department.objects.update(dept_id=deptid, DepartmentName=dept, Description=Disc)
       
    #     return redirect('/')

    
