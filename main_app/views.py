from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Penguin
from .forms import FeedingForm


class PenguinCreate(CreateView):
    model = Penguin
    fields = '__all__'

class PenguinUpdate(UpdateView):
  model = Penguin
  fields = ['breed', 'description', 'age']

class PenguinDelete(DeleteView):
  model = Penguin
  success_url = '/penguins/'

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
      feeding_form = FeedingForm()
      return render(request, 'penguins/detail.html', { 'penguin': penguin, 'feeding_form': feeding_form })


def add_feeding(request, penguin_id):
    	# create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.penguin_id = penguin_id
    new_feeding.save()
    return redirect('detail', penguin_id=penguin_id)