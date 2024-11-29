from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
information = ["one", 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

finance_data = {"2024":{"bills": 2000, "food": 100, "pay": 2100},
                "2023":{"bills": 2000, "food": 200, "pay": 2100},
                "2022":{"bills": 2000, "food": 300, "pay": 2100},
                "2021":{"bills": 2000, "food": 400, "pay": 2100},
                "2020":{"bills": 2000, "food": 500, "pay": 2100},
                "2019":{"bills": 2000, "food": 600, "pay": 2100}
                }


def home(request):
    return render(request, 'home.html', {'information': finance_data})


def year(request, pk):
    return HttpResponse('SINGLE YEAR')

def expense(request, pk):
    return HttpResponse('SINGLE EXPENSE')

def index(request):
    data_points = [
        {"label": "apple", "y": 10},
        {"label": "orange", "y": 15},
        {"label": "banana", "y": 25},
        {"label": "mango", "y": 30},
        {"label": "grape", "y": 28}
    ]

    label = ['apple', 'orange', 'banana', 'mango', 'grape']
    y = [10, 15, 25, 30, 28]
    return render(request, 'index.html', {"data_points": data_points, 'label': label, 'y': y})
