from .models import Teachers, Students, Categories, Courses, Comment, Chapter
from rest_framework import serializers


class TeachersSerializers(serializers.ModelSerializer):
	class Meta:
		model = Teachers
		fields = ("id", "first_name", "last_name", "username", "email", "password", "profile_pic" "user")


class StudentsSerializers(serializers.ModelSerializer):
	class Meta:
		model = Students
		fields = ("id", "first_name", "last_name", "username", "email", "password", "profile_pic", "user")


class CategoriesSerializers(serializers.ModelSerializer):
	class Meta:
		model = Categories
		fields = ("id", "name")


class CoursesSerializers(serializers.ModelSerializer):    
	class Meta:
		model = Courses
		fields = ("id", "title", "category", "teacher", "students", "difficulty", "description", "price", "last_update", "lectures", "duration")
		depth = 1

class CommentSerialezers(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ("id", "course", "comment", "student", "date_created", "rating")
		depth = 1


class ChapterSerializers(serializers.ModelSerializer):
	class Meta:
		model = Chapter
		fields = ("id", "course", "title", "description", "video", "video_duration")
		depth = 1
