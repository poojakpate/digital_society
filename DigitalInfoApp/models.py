from django.db import models
from .views import *

class Role(models.Model):
    Name = models.CharField(max_length=20)

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.Name

class Master(models.Model):
    Role = models.ForeignKey(Role,on_delete=models.CASCADE)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=15)
    Mobile=models.CharField(max_length=15)
    IsActive=models.BooleanField(default=False)

    class Meta:
        db_table='master'

class Society_member(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=20, default="")
    Mobile = models.CharField(max_length=10, default="")

    class Meta:
        db_table = 'society_member'

class Society_secretary(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=20, default="")
    Mobile = models.CharField(max_length=10, default="")

    class Meta:
        db_table = 'society_secretary'

 