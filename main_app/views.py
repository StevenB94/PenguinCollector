from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Penguin:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

penguins = [
  Penguin('Mac', 'macaroni', 'yellow', 3),
  Penguin('Sachi', 'emporer', 'black', 0),
  Penguin('Raven', 'chin strap', 'brown', 4)
]

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def penguins_index(request):
  return render(request, 'penguins/index.html', { 'penguins': penguins })