from django.db import models
from edubox.users.models import User


class Assignment(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class GradedAssignment(models.Model):
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    assignment = models.ForeignKey('base.Assignment', on_delete=models.SET_NULL, blank=True, null=True)
    grade = models.FloatField()

    def __str__(self):
        return self.student.username


class Choice(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=200)
    choices = models.ManyToManyField('base.Choice')
    answer = models.ForeignKey('base.Choice', on_delete=models.CASCADE, related_name='answer', blank=True, null=True)
    assignment = models.ForeignKey('base.Assignment', on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    order = models.SmallIntegerField()

    def __str__(self):
        return self.question

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    timeopen = models.IntegerField(default=0)
    timeclose = models.IntegerField(default=0)
    timelimit = models.IntegerField(default=0)
    attempts = models.IntegerField(default=1)



class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    favorite = models.BooleanField(default=False)

class PostFile(models.Model):
    post = models.ForeignKey('base.Post', on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='uploads/')
    

class Post(models.Model):
    course = models.ForeignKey('base.Course', on_delete=models.CASCADE, blank=True, null=True)    
    text = models.CharField(max_length=10000, blank=True, null=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    is_pinned = models.BooleanField(default=False, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)



    

