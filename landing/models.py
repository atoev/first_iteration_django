from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    teaching_course = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
