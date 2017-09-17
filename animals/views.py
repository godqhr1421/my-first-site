from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    return render(request, 'animals/home.html')

def history(request):

    return render(request, 'animals/history.html')

def animals(request):

    return render(request, 'animals/animals.html')

def solutions(request):

    return render(request, 'animals/solutions.html')


def rabbit(request):

    return render(request, 'animals/rabbit.html')

def dog(request):

    return render(request, 'animals/dog.html')

def monkey(request):

    return render(request, 'animals/monkey.html')
