from django.shortcuts import render

# Create your views here.
information = ["one", 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']




def home(request):
    return render(request, 'home.html', {'information': information})
