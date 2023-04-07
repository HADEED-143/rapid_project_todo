from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.IntegerField(primary_key=True, max_length=20)
    status = models.BooleanField(null=False, default=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

class Tasks(models.Model):
    id = models.ForeignKey(Users, on_delete=models.CASCADE, primary_key=True) #foreign
    status = models.BooleanField(null=False, default=True)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(start_date)


class Categories(models.Model):
    id = models.IntegerField(primary_key=True, max_length=20)
    title = models.CharField(null=False, max_length=50)
    status = models.BooleanField(default=False)

class Reminders(models.Model):
    id = models.IntegerField(primary_key=True, max_length=20)
    task_id = models.ForeignKey(Tasks , max_length=20, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, null=False)
    status = models.BooleanField(default=False)
    r_date = models.DateTimeField(auto_now_add=True)

