from django.shortcuts import render
from scoring.models import Judge, Judge_Assignment, Project
from scoring.views.display.unassigned_projects import unassigned_projects


def display_unassignedproject(request):
    context = {}
    context = unassigned_projects()
    return render(request, 'unassignedproject.html', context)
