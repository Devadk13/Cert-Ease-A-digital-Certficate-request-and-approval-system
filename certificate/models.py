from django.db import models

# Create your models here.

class Certificate(models.Model):
    c_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'certificate'
