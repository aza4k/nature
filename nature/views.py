from django.shortcuts import render

def home(request):
    return render(request,'nature/base.html')