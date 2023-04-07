from django.shortcuts import render

from base.forms import Users


# Create your views here.
def home(request):
    form = Users()
    context = {"form": form}
    return render(request, 'home.html', context)
"""
def Tasks(request):
    form = Tasks()
    context = {"form": form}
    return render(request, 'home.html', context)

def Categories(request):
    form = Categories()
    context = {"form": form}
    return render(request, 'home.html', context)

def Reminders(request):
    form = Reminders()
    context = {"form": form}
    return render(request, 'home.html', context)"""