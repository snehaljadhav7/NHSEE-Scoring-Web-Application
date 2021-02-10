from scoring.models import Project

def cal_scaled_z_score():
    projects = list(Project.objects.all())
    for index in range(len(projects)):
        min = list(Project.objects.all().order_by('z_score'))[index].z_score
        if min is not None:
            break
    for index in range(len(projects)):
        max = list(Project.objects.all().order_by('-z_score'))[index].z_score
        if max is not None:
            break
    if max is None or min is None:
         return
    rangevalue = max - min
    for project in projects:
        if project.z_score is None:
            continue
        project.scaled_z = ((project.z_score - min)/rangevalue)*25 + 25
        project.save()
