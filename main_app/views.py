from django.shortcuts import render

# Add the following import
from .models import Penguin


# Define the home view
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def penguins_index(request):
    penguins = Penguin.objects.all()
    return render(request, 'penguins/index.html', { 'penguins': penguins })


def penguins_detail(request, penguin_id):
      penguin = Penguin.objects.get(id=penguin_id)
      return render(request, 'penguins/detail.html', { 'penguin': penguin })