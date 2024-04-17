from django.shortcuts import render

# Create your views here.
def ttest(request):
    print('test working')
    return render(request, 'htmlwork/templates/life/index.html')