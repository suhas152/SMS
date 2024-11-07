from django.db import models
from django.shortcuts import render


class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'


class StudentList(models.Model):
    Register_Number = models.CharField(max_length=10, unique=True)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Register_Number


def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})





class feedback(models.Model):
    name = models.CharField(max_length=100,default='Anonymous')
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10)
    textfield = models.TextField(max_length=150, default='No comments provided')

    def str(self):
        return self.name

class Manager(models.Model):
    name = models.CharField(max_length=100, default='Anonymous')
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=10)

    def str(self):
        return self.name
