from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

	USER_STATUS = (
		('Admin', 'Admin'),
		('Teacher', 'Teacher'),
		('Student', 'Student'),
	)

	first_name = models.CharField(max_length=64, null=True, blank=True)
	last_name = models.CharField(max_length=64, null=True, blank=True)
	username = models.CharField(max_length=32, unique=True)
	email = models.CharField(max_length=64, unique=True)
	password = models.CharField(max_length=32, unique=True)
	profile_pic = models.ImageField(null=True, blank=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=16, choices=USER_STATUS)


class Categories(models.Model):
	name = models.CharField(max_length=64)


	def __str__(self):
		return self.name


class Courses(models.Model):

	DIFFICULTY_CHOICES = (
		('Easy', 'Easy'),
		('Medium', 'Medium'),
		('Hard', 'Hard'),
	)

	title = models.CharField(max_length=128)
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='category_courses')
	teacher = models.ManyToManyField(Teachers, related_name="teacher_courses")
	students = models.ManyToManyField(Students)
	difficulty = models.CharField(max_length=16, choices=DIFFICULTY_CHOICES)
	description = models.CharField(max_length=256, null=True)
	price = models.IntegerField(null=False)
	last_update = models.DateTimeField(auto_now_add=True) 
	lectures = models.IntegerField()
	duration = models.PositiveBigIntegerField()


	def __str__(self) -> str:
		return self.title


class Comment(models.Model):
	course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="course_comments")
	comment = models.TextField(max_length=2048)
	student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='student_comments')
	date_created = models.DateTimeField(auto_now_add=True)
	rating = models.FloatField()


class Chapter(models.Model):
	course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="course_chapters")
	title = models.CharField(max_length=256)
	description = models.TextField(max_length=2048)
	video = models.FileField(upload_to="chapter_videos", null=True, blank=True)
	video_duration = models.PositiveIntegerField()


	def __str__(self):	
		return self.title
		