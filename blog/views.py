from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from .models import Entry, Author, Comment, Blog

# Create your views here.
class CreateEntryView(CreateView):
    model = Entry
    template_name = 'blog/create.html'
    fields = ['blog', 'headline', 'body_text', 'authors']
    success_url = '/blog/'

class UpdateEntryView(UpdateView):
    model = Entry
    template_name = 'blog/update.html'
    fields = ['blog', 'headline', 'body_text', 'authors']
    success_url = '/blog/'

class DeleteEntryView(DeleteView):
    model = Entry
    #template_name = 'blog/delete.html'
    success_url = '/blog/' #reverse_lazy('index')

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_entries'
    def get_queryset(self):
        return Entry.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:3]
    
