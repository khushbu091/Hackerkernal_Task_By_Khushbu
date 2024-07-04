from django.db import models

# Create your models here.
class User(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=50)
    Email = models.EmailField()
    MOBILE = models.IntegerField()
    class Meta:
        db_table = 'User'
    def __str__(self):
        return self.NAME

class Task(models.Model):
    Task={
        "Pending":"pending",
        "Done":"done",
    }
    Task_details=models.TextField(max_length=50)
    Task_type=models.CharField(max_length=50, choices=Task)
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return str(self.Task_details) 