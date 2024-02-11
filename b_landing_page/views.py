from django.shortcuts import render

# Create your views here.
def landing_page(request):
    content = {
        'title': 'Landing Page'
        }
    return render(request, 'b_landing_page/landing_page.html', content)