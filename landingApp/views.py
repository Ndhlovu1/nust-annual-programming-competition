from django.shortcuts import render

#Landing
def landing_page(request):
    return render(request, 'landingApp/landing_page.html')
