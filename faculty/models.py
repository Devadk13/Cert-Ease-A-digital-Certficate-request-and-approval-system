from django.db import models
from department.models import Department

# Create your models here.

class Faculty(models.Model):
    f_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    # d_id = models.IntegerField()
    d=models.ForeignKey(Department, to_field='d_id', on_delete= models.CASCADE)
    contact_no = models.CharField(max_length=45)
    email_id = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'faculty'

