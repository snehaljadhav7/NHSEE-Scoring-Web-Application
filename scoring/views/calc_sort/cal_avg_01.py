from scoring.models import Judge_Assignment, Project
from statistics import mean

def cal_avg_01():
    projects = list(Project.objects.all())
    for project in projects:
        jas = Judge_Assignment.objects.filter(project_id = project.project_id)
        all_judge_z_ranks = []
        for ja in jas:
            if ja.raw_score != 0:
                all_judge_z_ranks.append(ja.rank)
        if len(all_judge_z_ranks) < 2:
            continue
        project.avg_01 = mean(all_judge_z_ranks)
        project.save()
