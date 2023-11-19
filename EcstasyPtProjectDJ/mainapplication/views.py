from django.shortcuts import render

def about_page(request):
    return render(request,'mainapplication/about_page.html')

def contacts_page(request):
    return render(request,'mainapplication/contacts_page.html')