from django.shortcuts import render

def home_view(request):
    # Try this first - using app templates
    return render(request, '../templates/home.html')
    
    # If that doesn't work, try the project templates:
    # return render(request, 'home.html')clscls