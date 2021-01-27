from django.db import models

# Create your models here.
class Survey(models.Model):
    rnum = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=4)
    age = models.IntegerField()
    co_survey = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'survey'
