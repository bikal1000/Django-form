from django.shortcuts import render
from .models import Form

# Create your views here.
def index(request):
    return render(request,'form/index.html')

def forms(request):
    
    if request.method == 'POST':
        username_r=request.POST.get('username')
        email_r=request.POST.get('email')

        c=Form(username=username_r,email=email_r)
        c.save()
        return render(request,'form/form.html')
       

    else:
        return render(request,'form/form.html')


       

    