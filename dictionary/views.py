from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.views.generic.edit import FormView
import json

from .models import Dictionary

# index to dictionary app, allowing to search words
def index(request):
    word = ''
    definitions = []
    if 'word' in request.GET:
        word = request.GET['word']
        if len(word)>0:
            definitions = Dictionary.objects.filter(
                word__icontains=word).order_by('word')
    context = {"definitions": definitions}
    return render(request, 'dictionary/index.html', context)

# view to add new word and definition pairs to dictionary
def addview(request):
    context = {}
    return render(request, 'dictionary/addview.html', context)    

# make a form from a model (easy and lazy way :) )
class DictionaryForm(ModelForm):
    class Meta:
        model = Dictionary
        fields = ['word', 'definition']

# add new words to dictionary
def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DictionaryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            word = form.cleaned_data['word']
            definition = form.cleaned_data['definition']
            # save to dictionary
            d = Dictionary(word=word, definition=definition)
            d.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('dictionary:addview'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = DictionaryForm()
    return render(request, 'dictionary/addview.html', {'form': form})    

# AJAX version to add words to dictionary
def addjson(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if "word" in request.POST and "definition" in request.POST:
            word = request.POST['word']
            definition = request.POST['definition']
            # save to dictionary
            if len(word)>0 and len(definition)>0:
                d = Dictionary(word=word, definition=definition)
                d.save()
                return JsonResponse("success", safe=False)
    return JsonResponse("failure", safe=False)

# this is only used for the AJAX version of the search    
def search(request):
    def_list = [];
    if 'word' in request.GET:
        word = request.GET['word']
        if len(word)>0:
            definitions = Dictionary.objects.filter(word__icontains=word)
            def_list = [str(definition) for definition in definitions]
    def_json = json.dumps(def_list)
    return JsonResponse(def_json, safe=False)
    
