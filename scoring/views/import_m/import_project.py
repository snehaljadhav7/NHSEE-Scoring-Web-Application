from scoring.models import Project
from scoring.views import convertStrToNum as c


def import_project(sheet):
    for s in range(5, 66):
        project_id = sheet['D'+str(s)].value
        table_id = sheet['C'+str(s)].value
        description = sheet['L'+str(s)].value
        project_title = sheet['J'+str(s)].value
        project_category = sheet['K'+str(s)].value
        avg_score = None
        rank = None
        z_score = None
        z_score_rank = None
        avg_01 = None
        avg_01_rank = None
        scaled_score = None
        scaled_rank = None
        scaled_z = None
        isef_score = None
        isef_rank = None

        p = Project(project_id, c.int1(table_id), description, project_title,
                    project_category, c.float1(avg_score), c.int1(rank),
                    c.float1(z_score), c.float1(scaled_score),
                    c.float1(scaled_rank), c.float1(scaled_z),
                    c.float1(isef_score), c.int1(isef_rank))
        p.save()
