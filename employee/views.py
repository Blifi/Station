from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm 
from employee.serializers import SnippetSerializer 
from employee.models import Employee
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.  
@api_view(['GET', 'POST'])
def emp(request):
    
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        breakpoint()
        if form.is_valid:
            try:  
                form.save()
                return redirect('/show')  
            except:  
                pass
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
@api_view(['GET', 'POST'])
def empapi(request):
    
    if request.method == "POST":
        form = EmployeeForm(request.data)
        form.is_valid()
        form = EmployeeForm(request.data)
        #breakpoint()
        if form.is_valid:
            try:  
                form.save()
                return redirect('/show')  
            except:  
                pass
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})   
    
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  
    
class ToDoViews(APIView):
#    def get(self, request):
#        return Response({'test': 'It worked!'})
    def post(self, request):
        print(request.data)
        return Response({"id": 'anyClass',
                     "data": '1234',
               })