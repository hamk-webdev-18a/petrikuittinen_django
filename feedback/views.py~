from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import widgets
from django import forms

# Create your views here.
from .models import Feedback

class FeedbackView(LoginRequiredMixin, CreateView):
    model = Feedback
    template_name = 'feedback/index.html'
    fields = ['good', 'bad', 'ideas']
    success_url = 'thanks/'

    
# manually created form
class FeedbackForm(forms.Form):
    good = forms.CharField(label='Good', max_length=1000,
                           widget=widgets.Textarea)
    bad = forms.CharField(label='Bad', max_length=1000,
                          widget=widgets.Textarea)
    ideas = forms.CharField(label='Ideas', max_length=1000,
                            widget=widgets.Textarea)

    
@login_required(login_url='/login/')
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            good = form.cleaned_data['good']
            bad = form.cleaned_data['bad']
            ideas = form.cleaned_data['ideas']
            f = Feedback(good=good, bad=bad, ideas=ideas)
            f.save()
            # redirect to a new URL:
            return HttpResponseRedirect('thanks/')
    else:
        # if method is 'GET' then create an empty form
        form = FeedbackForm()
        return render(request, 'feedback/index.html', {'form': form})
        
def thanks(request):
    return render(request, 'feedback/thanks.html', {})
                                                    
