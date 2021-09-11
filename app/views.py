from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fun_form(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        return render(request,'second.html',context={'un':username,'pw':password})
    return render(request,'first.html')
