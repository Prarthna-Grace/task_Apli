import datetime
import datetime
from django.utils import timezone
from django.db import models

class AllLevels(models.Model):
    Levelname= models.CharField(max_length=300)
    testname=models.CharField(max_length=300)
    startedfrom=models.DateTimeField('Started from')
    def __str__(self):
        return self.testname
    def was_published_recently(self):
        return self.startedfrom >=timezone.now()- datetime.timedelta(days=10)

class details(models.Model):
    test=models.ForeignKey(AllLevels, on_delete=models.CASCADE)
    ct=models.CharField(max_length=500)
    your_choice=models.BooleanField(default=False)

    def __str__(self):
        return str(self.ct)