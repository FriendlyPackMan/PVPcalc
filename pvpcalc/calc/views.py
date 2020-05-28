from django.shortcuts import render

# Create your views here.
def calc(request):
    return render(request, 'calc/main.html')