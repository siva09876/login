from django.shortcuts import render ,redirect
from django.urls import reverse
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .forms import studentform,Student_Form
from .models import *
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .tests import *
# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None :
            print(user.is_employee)
            login(request,user)
            print(user)
            return redirect(reverse('main'))
        else:
            messages.warning(request,'invalid password')
            return render(request,'login/home.html')
    else:
        return render(request,'login/home.html')

@login_required(login_url='home')
def main(request):

    if request.method == 'POST':
        user=request.user
        form = Student_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.user=user
            print(user)
            form.save()
            body=f'Hey {user}! your complaint was registered successfully. You can track the complaint with the tracking id. Complaint will be solved within 2 working days. Thank You'
            reciever=user.email
        
            
            
            return redirect('home')
    else:
        form=Student_Form()
    return render(request,'login/main.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = studentform()   
    return render(request, 'login/register.html', {'form': form})

def complaint(request):
    obj=StudentForm.objects.all()
    return render(request,'login/complaint.html',{'obj':obj})


def update_status(request,pk):
    obj=StudentForm.objects.get(id=pk)
    form=Student_Form(instance=obj)
    if request.method=='POST':
        form=Student_Form(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('complaint')
    context={
        'form':form
    }
    return render (request,'login/update.html',context=context)