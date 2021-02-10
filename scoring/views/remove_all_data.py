from scoring.models import *
from django.shortcuts import render
from django.contrib import messages


def remove_all_data(request):
    if request.method == 'POST':
        try:
            Judge.objects.all().delete()
            Project.objects.all().delete()
            Student.objects.all().delete()
            Judge_Assignment.objects.all().delete()
            messages.success(request, "Data deleted successfully")
        except Exception:
            messages.success(request, "Error")

    return render(request, 'delete.html')
