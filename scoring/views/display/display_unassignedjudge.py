from django.shortcuts import render
from scoring.models import Judge, Judge_Assignment, Project
from scoring.views.display.unassigned_judges import unassigned_judges


def display_unassignedjudge(request):
    context = {}
    context = unassigned_judges()
    return render(request, 'unassignedjudge.html', context)
