from django.shortcuts import render

def main_page(request):
    matter_data = {
        'something_not_wrong': ['depre??ed', 'scareº', 'alone..'],
        'morphe_ya': {
            'name':'Lerochka',
            'yo':21,
            'city':'sochy',
            'lovely people':'gleb = lovely lovely 🖤'
        }
    }
    return render(request,'mainapplication/main_page.html', matter_data)

def about_page(request):
    return render(request,'mainapplication/about_page.html')

def contacts_page(request):
    return render(request,'mainapplication/contacts_page.html')