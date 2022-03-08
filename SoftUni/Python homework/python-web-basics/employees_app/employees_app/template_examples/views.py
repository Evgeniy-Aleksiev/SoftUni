from django.shortcuts import render

from employees_app.employees.models import Employee, Department


def index(request):
    context = {
        'number_1': 123,
        'number_2': 321,
        'number_3': 200,
        'numbers': [123, 321, 200],
        'filesize': 12345678,
        'title': 'emplOYees list',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut deserunt eum expedita illum possimus suscipit. Accusamus amet architecto consequuntur dignissimos ducimus minus non officia optio praesentium repellat sit, suscipit voluptate!',
        'employees': Employee.objects.all(),
        'department_names': [d.name for d in Department.objects.all()]
    }
    return render(request, 'templates_examples/index.html', context)
