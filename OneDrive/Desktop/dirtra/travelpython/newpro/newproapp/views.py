from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django .shortcuts import render
from . models import Place
from . models import Team
def demo(request):
    obj=Place.objects.all()
    obje=Team.objects.all()
    return render(request,"index.html",{'result':obj,'resu':obje})



#def addition(request):

  #      x=int(request.GET['ist_num'])
   #     y=int(request.GET['2nd_num'])
    #    p=x+y
     #   q=x-y
      #  r=x*y
       # s=x/y
        #return render(request,"result.html",{'res1':p,'res2':q,'res3':r,'res4':s})
