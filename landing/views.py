from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def team(request):
    return render(request, "team.html")

def activities(request):
    return render(request, "activities.html")

def contact(request):
    return render(request, "contact.html")

def portfolio(request):
    return render(request, "portfolio.html")

def donate(request):
    return render(request, "donate.html")