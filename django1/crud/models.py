from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Player(models.Model):
    pname = models.CharField(max_length=50)
    pnickname = models.CharField(max_length=50)
    pno = models.IntegerField()
    pscore = models.IntegerField()
    pbirthdate = models.DateField()
    pstatus = models.BooleanField()
    
    class Meta:
        db_table = "player"
        
        