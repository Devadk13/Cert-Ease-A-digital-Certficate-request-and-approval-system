from django.db import models

# Create your models here.

class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'department'

