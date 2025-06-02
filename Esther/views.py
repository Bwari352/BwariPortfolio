from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'base.html')

# def homePage(request):
#    return render(request, 'homePage.html')
#
