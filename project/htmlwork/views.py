from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.
def life_index(request): return render(request, 'life/index.html')

def life_sub01(request): return render(request, 'life/sub01.html')
def life_sub01_02(request): return render(request, 'life/sub01_02.html')
def life_sub01_03(request): return render(request, 'life/sub01_03.html')
def life_sub01_04(request): return render(request, 'life/sub01_04.html')

def life_sub02(request): return render(request, 'life/sub02.html')
def life_sub02_02(request): return render(request, 'life/sub02_02.html')
def life_sub02_03(request): return render(request, 'life/sub02_03.html')

def life_sub03(request): return render(request, 'life/sub03.html')
def life_sub04(request): return render(request, 'life/sub04.html')
def life_sub04_02(request): return render(request, 'life/sub04_02.html')
