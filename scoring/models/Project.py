from django.db import models

class Project(models.Model):
    project_id = models.CharField(primary_key=True, max_length=6)
    table_id = models.IntegerField(null=True)
    description = models.CharField(max_length=1000,null=True)
    project_title = models.CharField(max_length=500)
    project_category = models.CharField(max_length=100)
    avg_score = models.FloatField(null=True)
    rank = models.IntegerField(null=True)
    z_score = models.FloatField(null=True)
    z_score_rank = models.IntegerField(null=True)
    avg_01 = models.FloatField(null=True)
    avg_01_rank = models.IntegerField(null=True)
    scaled_score = models.FloatField(null=True)
    scaled_rank = models.FloatField(null=True)
    scaled_z = models.FloatField(null=True)
    isef_score = models.FloatField(null=True)
    isef_rank = models.IntegerField(null=True)
    category_rank = models.IntegerField(null=True)
    fair_rank = models.IntegerField(null=True)
    no_show = models.BooleanField(default=False)

    def __str__(self):
        return self.project_id
