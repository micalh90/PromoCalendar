from django.shortcuts import render

# Create your views here.

def user_login(request):
    content = { 
        'title': 'Login'
        }
    
    return render(request, 'b_user_auth/login.html', content)