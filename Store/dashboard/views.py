from django.shortcuts import render

def dashboard(request):
    data={}
    return render(request,'dashboard.html', data)
