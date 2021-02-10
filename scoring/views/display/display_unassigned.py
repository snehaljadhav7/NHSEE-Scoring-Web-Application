from django.shortcuts import render
from scoring.models import Judge, Judge_Assignment, Project
from scoring.views.display.unassigned_judges import unassigned_judges
from scoring.views.display.unassigned_projects import unassigned_projects


def display_unassigned(request):
    context = {}
    judges_dict = unassigned_judges()
    projects_dict = unassigned_projects()
    context["button"] = 'button'
    context["unassigned_judges"] = judges_dict["unassigned_judges"]
    context["unassigned_projects"] = projects_dict["unassigned_projects"]

    return render(request, 'unassigned.html', context)
