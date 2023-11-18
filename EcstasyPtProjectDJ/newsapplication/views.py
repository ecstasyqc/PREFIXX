from django.shortcuts import render, redirect
from .models import Articles
from .forms import AcriclesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Articles.objects.all()
    return render(request,'newsapplication/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'newsapplication/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'newsapplication/update_page.html'

    form_class = AcriclesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'newsapplication/delete_page.html'

def create_page(request):
    error = ''
    if request.method == 'POST':
        form = AcriclesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Form was braked, try again: '

    form = AcriclesForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'newsapplication/creat_page.html', data)