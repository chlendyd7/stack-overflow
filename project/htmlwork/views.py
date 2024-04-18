from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.
def life_index(request):
    print('test working')
    return render(request, 'life/index.html')

def life_sub02(request):
    return render(request, 'life/sub02.html')
    # return HttpResponse(render_to_string('life/sub02.html'))

def life_sub02_02(request):
    return render(request, 'life/sub02_02.html')