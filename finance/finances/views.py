from django.shortcuts import render

# Create your views here.
information = ["one", 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']




def home(request):
    return render(request, 'home.html', {'information': information})


def index(request):
    data_points = [
        {"label": "apple", "y": 10},
        {"label": "orange", "y": 15},
        {"label": "banana", "y": 25},
        {"label": "mango", "y": 30},
        {"label": "grape", "y": 28}
    ]
    return render(request, 'index.html', {"data_points": data_points})
