from django.db import models
from certificate.models import Certificate
from student.models import Students
from faculty.models import Faculty
# Create your models here.

class Request(models.Model):
    r_id = models.AutoField(primary_key=True)
    # c_id = models.IntegerField()
    c= models.ForeignKey(Certificate,to_field='c_id',on_delete=models.CASCADE)
    # s_id = models.IntegerField()
    student=models.ForeignKey(Students,to_field='student_id',on_delete=models.CASCADE)
    # f_id = models.IntegerField()
    f=models.ForeignKey(Faculty, to_field='f_id',on_delete=models.CASCADE)
    need = models.CharField(max_length=45)
    date = models.DateField()
    status = models.CharField(max_length=45)
    reject_reason = models.CharField(max_length=45)
    uploaded_documents = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'request'
