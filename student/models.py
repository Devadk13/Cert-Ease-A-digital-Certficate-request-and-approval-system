from django.db import models
from department.models import Department
from faculty.models import Faculty
# Create your models here.
class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    contact_no = models.CharField(max_length=45)
    email_id = models.CharField(max_length=45)
    # d_id = models.IntegerField()
    d= models.ForeignKey(Department,to_field='d_id', on_delete=models.CASCADE)
    batch = models.CharField(max_length=45)
    year = models.CharField(max_length=45)
    # f_id = models.IntegerField()
    f= models.ForeignKey(Faculty,to_field='f_id', on_delete=models.CASCADE)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'students'

