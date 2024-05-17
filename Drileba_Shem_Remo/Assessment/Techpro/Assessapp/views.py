from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from Assessapp import views as auth_views

# Create your views here.
def index (request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been successfully submitted!')
            return redirect('index')
        else:
            messages.error(request, 'Form has some invalid fields!')
    else:
        form = RegForm()
    return render(request, 'Assessapp/index.html', {'form': form})