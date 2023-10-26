from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
# def demo(request):
#     return.html render(request,'demo.html')
# def demo(request):
#     return.html render(request,'base.html')


from django.http.response import HttpResponse
from django.shortcuts import render
from .models import district, Branch
from django.core import serializers
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib import auth
from django.contrib import messages,auth


def demo(request):
   return render(request, "index.html")
def loginn(request):
   if request.method == 'POST':
      username=request.POST['username']
      password=request.POST['password']
      user=auth.authenticate(username=username,password=password)
      if user is not None:
         auth.login(request,user)
         return redirect('new')
      else:
         messages.info(request,"invalid username")
         return redirect('loginn')
   else:
      return render(request,"login.html")
def register(request):
   if request.method == 'POST':
      username=request.POST['username']
      password = request.POST['password']
      password1 = request.POST['password1']
      if password == password1:
         if User.objects.filter(username=username).exists():
            messages.info(request,"usernametaken")
            return redirect(register)
         else:
            user=User.objects.create_user(username=username,password=password)
            user.set_password(password)
            user.save()
            print("user created")
            return redirect(loginn)


      else:
         messages.info(request,'both passwords are not matching')
         return redirect(register)
   else:
      print("no post method")
      return render(request,'register.html')


def logout(request):
   auth.logout(request)
   return redirect('/')

def new(request):
   return render(request,"new.html")

def form(request):
   return render(request,"return.html")



from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import district, Branch
from django.core import serializers
import json


# Create your views here.

def getdata(request):
   template_name = 'dropdown.html'
   deptcontext = district.objects.all()
   empcontext = Branch.objects.all()

   return render(request, template_name, {'department': deptcontext, 'employee': empcontext})

# Create your views here.
def message(request):
   return render(request,'return.html')