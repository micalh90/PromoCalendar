from django.shortcuts import render


# Create your views here.
def landing_page(request):
    content = {
        'title': 'Landing Page'
        }
    return render(request, 'landing_page.html', content)

def user_login(request):
    content = {
        'title': 'User Login'
        }
    return render(request, 'user_login.html', content)

def user_create(request):
    content = {
        'title': 'User Create'
        }
    return render(request, 'user_create.html', content)