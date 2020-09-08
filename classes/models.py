from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	subject = models.CharField(max_length=120)
	grade = models.IntegerField(default = 0)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

	def __str__(self):
		return self.subject

class Student(models.Model):
	name = models.CharField(max_length=120)
	dob = models.DateField()
	GENDER_CHOICES = (('F', 'Female',),('M', 'Male',),)
	gender = models.CharField(max_length=7, choices = GENDER_CHOICES, default="Male")
	exam_grade = models.IntegerField()
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="students")



	def __str__(self):
		return self.name
