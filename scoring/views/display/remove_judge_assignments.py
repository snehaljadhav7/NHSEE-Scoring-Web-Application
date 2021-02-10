from django.shortcuts import render
from scoring.models import Project, Judge_Assignment
from scoring.models import Judge
from django.contrib import messages


def remove_assigned_judge_assignments(request):
    items_judge = Judge.objects.all()

    judge_list = []
    unassigned_judges = []
    assigned_projects = []
    assigned_judges = []

    for judge in items_judge:
        judgestatus = Judge_Assignment.objects.filter(judge_id=judge.judge_id)
        assign_judge_list = []
        graded = 0

        for ja in judgestatus:
            assign_judge_list.append(ja.judge_id)
            if ja.raw_score != 0:
                graded = graded + 1
        projects_assigned = len(assign_judge_list)
        if projects_assigned > 0:
            assigned_judges.append({"judge_name": str(judge.name),
                                    "judge_id": judge.judge_id})

    button = "judges"
    context = {
            'button': button,
            'assigned_judges': assigned_judges,

        }
    return render(request, 'removeassignmentsjudges.html', context)


def deletejudgeassignment(request):
    if request.method == "POST":
        judge_id = request.POST['judge']
        judge = Judge.objects.get(judge_id=judge_id)

        Judge.objects.get(judge_id=judge_id).delete()
    return render(request, 'home.html')
