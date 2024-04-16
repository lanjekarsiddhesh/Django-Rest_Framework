from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=500)
    Roll_number = models.BigIntegerField()

    class Meta:
        db_table = 'student'
        
    def __str__(self):
        return self.first_name + ' ' + self.last_name
