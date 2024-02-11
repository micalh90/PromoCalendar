from django.shortcuts import render

# Create your views here.

def user_login(request):
    content = { 
        'title': 'Login'
        }
    
    return render(request, 'b_user_auth/login.html', content)

def user_create(request):
    content = {
        'title': 'Create'
        }
    return render(request, 'b_user_auth/create_user.html', content)