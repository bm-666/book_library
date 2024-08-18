from django.shortcuts import render



def auth_page(request):
    return render(request, 'base/base_auth_page.html')