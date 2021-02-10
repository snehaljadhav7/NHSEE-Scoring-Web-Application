from django.shortcuts import render
from scoring.models import Judge, Judge_Assignment, Project
from django.contrib import messages
from scoring.views.display.unassigned_judges import unassigned_judges
from scoring.views.display.unassigned_projects import unassigned_projects
def display_unasigned(request):
    context = {}
    judges_dict = unassigned_judges()
    projects_dict = unassigned_projects()
    context["button"] = 'button'
    context["unassigned_judges"] = judges_dict["unassigned_judges"]
    context["unassigned_projects"] = projects_dict["unassigned_projects"]

    return render(request, 'assigned.html', context)



def createjudgeassignment(request):
    if request.method == "POST":
        context = {}
        project_id = request.POST['project']
        judge_id = request.POST['judge']

        project =  Project.objects.get(project_id = project_id)
        judge = Judge.objects.get(judge_id = judge_id)

        Judge_Assignment(judge_id = judge, project_id = project, goal_score = 0, plan_score = 0, action_score = 0, result_analysis_score = 0, communication_score = 0, raw_score = 0, z_score = 0, rank = 0   ).save()


    return render(request, 'home.html')
