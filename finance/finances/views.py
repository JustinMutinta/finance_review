from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

finance_data = {
    "2024":{
        "January": {
            "bills": 3000, "food": 1000, "pay": 2000
        },
        "February": {
            "bills": 2000, "food": 2000, "pay": 3000
        },
        "March": {
            "bills": 1000, "food": 3000, "pay": 4000
        }
    },
    "2023":{
        "January": {
            "bills": 7000, "food": 4000, "pay": 5000
        },
        "February": {
            "bills": 6000, "food": 5000, "pay": 6000
        },
        "March": {
            "bills": 5000, "food": 6000, "pay": 7000
        }
    }
}


def home(request):
    return render(request, 'home.html', {'information': finance_data})

def year(request, pk):
    expense_axis = {
        "2024": { "January" : { "income": 5000, "outcome": 2000 },
                  "February" : { "name" : {"income", "outcome"}, "cost": {5000, 3000} }
        },
        "2023": { "February" : {"income": 6000, "outcome": 3000 } }
    }

    return render(request, 'year.html', {'pk': pk,
                                         'expense_axis': expense_axis})

def month(request, year, month):
    expense_axis = []
    cost_axis = []
    for item in finance_data[year][month]:
        expense_axis.append(item)
        cost_axis.append(finance_data[year][month][item])

    return render(request, 'month.html', {'year': year,
                                          'month': month,
                                          'expense_axis': expense_axis,
                                          'cost_axis': cost_axis})

def expense(request, pk):
    return render(request, 'expense.html', {'pk': pk})

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
