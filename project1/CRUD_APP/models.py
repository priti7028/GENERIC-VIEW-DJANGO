from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.IntegerField()
    C_name = models.CharField(max_length=100)
    c_fees = models.FloatField()

    def __str__(self):
        return self.id