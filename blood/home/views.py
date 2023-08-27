from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def donor(request):
    return render(request, "donor.html")

def search(request):
    return render(request, "search.html")

def admin(request):
    return render(request, "admin.html")

def contact(request):
    return render(request, "contact.html")
