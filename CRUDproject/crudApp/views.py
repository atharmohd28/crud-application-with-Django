from django.shortcuts import render
from django.shortcuts import redirect 
from .forms import StudentForm  
from .models import Student 
from django.contrib import messages
# Create your views here.

# ============Here start add student==================================================

def addStudent(request):
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Student Added Successfully')
    fm = StudentForm()
    studata = Student.objects.all()
    return render(request, 'index.html', context={'fm': fm, 'studata': studata})


# ============================here start delete student==============================================
def deleteStudent(request, id):
    Student.objects.get(pk=id).delete()
    messages.success(request, 'Student Record Deleted')
    return redirect('/')

# ==============================Herre start edit student============================================
def edit(request, id):
    instance = Student.objects.get(pk=id)
    if request.method == "POST":
        fm = StudentForm(request.POST, instance=instance)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Student Record Updated')
            return redirect('/')
    fm = StudentForm(instance=instance)
    return render(request, 'edit.html', context={'fm': fm})
