from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, 'app2_templates/home/home.html')


def analytics(request):
    return render(request, 'app2_templates/home/analytics.html')
