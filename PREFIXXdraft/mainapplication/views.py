from django.shortcuts import render

def main_page(request):
    return render(request, 'mainapplication/main_page.html')
def about_page(request):
    return render(request,'mainapplication/about_page.html')

def contacts_page(request):
    return render(request,'mainapplication/contacts_page.html')