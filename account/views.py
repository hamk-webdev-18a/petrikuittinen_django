from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'account/home.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            #return HttpResponseRedirect(reverse('home'))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


# this is not used, just an example show how to do a custom logout
def logout_view(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home')) # Redirect to a success

                                                    
