from django.shortcuts import render
from scoring.models import Project, Judge_Assignment
from scoring.models import Judge
from django.contrib import messages


def remove_assigned_project_assignments(request):
    items = Project.objects.all()
    item = Judge.objects.all()
    project_list = []
    assigned_projects = []
    for project in items:
        projectstatus = Judge_Assignment.objects.filter(project_id=project.project_id)
        assign_project_list = []
        graded = 0

        for ja in projectstatus:
            assign_project_list.append(ja.project_id)
            if ja.raw_score != 0:
                graded = graded + 1

        judges_assigned = len(assign_project_list)
        if judges_assigned > 0:
            assigned_projects.append({"project_id": project.project_id,
                                      "project_title": project.project_title})
    button = "projects"
    context = {
            'button': button,
            'assigned_projects': assigned_projects,

        }
    return render(request, 'removeassignmentsprojects.html', context)


def deleteprojectassignment(request):
    if request.method == "POST":
        project_id = request.POST['project']
        project = Project.objects.get(project_id=project_id)
        Project.objects.get(project_id=project_id).delete()
    return render(request, 'home.html')
