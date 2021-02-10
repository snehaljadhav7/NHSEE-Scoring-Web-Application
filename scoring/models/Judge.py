from django.db import models

class Judge(models.Model):
    judge_id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=10)
    no_show = models.BooleanField(default=False)


    def __str__(self):
        return '%s' %self.judge_id
        # to return a human-readable string for each object
