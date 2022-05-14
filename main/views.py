from re import T
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView


from .models import Teachers, Students, Categories, Courses, Comment, Chapter
from .serializers import (TeachersSerializers, StudentsSerializers, CategoriesSerializers,
						 CoursesSerializers, CommentSerialezers, ChapterSerializers)


class StudentSignup(APIView	):
	def get(self, request):
		return Response()


	def post(self, request):
		serializer = StudentsSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

class TeacherSignup(APIView	):
	def get(self, request):
		return Response()


	def post(self, request):
		serializer = TeachersSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

class login(APIView):
	def get(self, request):
		return Response()


	def post(self, request):
		data = request.data
		email = data.get("email")
		password = data.get("password")
		user = Students.get_student_by_email(email)
		error_message = None
		if user:
			if password == user.password:
				serializer = StudentsSerializers(user)
				return Response(serializer.data)
			else:
				error_message = 'Email or Password invalid !!'
		else:
			user = Teachers.get_teacher_by_email(email)
			print(user)
			if user:
				if password == user.password:
					serializer = TeachersSerializers(user)
					print("successfully")
					return Response(serializer.data)
				else:
					error_message = 'Email or password invalid !!'
			else:
				error_message = 'Email or Password invalid !!'

		return Response({'error': error_message})


class Profile(APIView):
	def get(self, request):
		print(request)
		return Response(True)


class AdminDashboard(APIView):
	def get(self, request):
		courses = Courses.objects.all()
		serializer = CoursesSerializers(courses, many=True)
		return Response(serializer.data)


class TeacherDashboard(APIView):
	def get(self, request):
		courses = Courses.objects.all()
		serializer = CoursesSerializers(courses, many=True)
		return Response(serializer.data)


class StudentDashboard(APIView):
	def get(self, request):
		courses = Courses.objects.all()
		serializer = CoursesSerializers(courses, many=True)
		return Response(serializer.data)


class CourseList(APIView):
	def get(self, request):
		courses = Courses.objects.all()
		serializer = CoursesSerializers(courses, many=True)
		return Response(serializer.data)
	

class CourseDetail(APIView):
	def get(self, request, pk):
		course = Courses.objects.get(pk=pk)
		serializer = CoursesSerializers(course)
		return Response(serializer.data)
	





#   test view, test view	

class StudentListView(generics.ListCreateAPIView):
	queryset = Students.objects.all()
	serializer_class = StudentsSerializers


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Students.objects.all()
	serializer_class = StudentsSerializers


class TeacherListView(generics.ListCreateAPIView):
	queryset = Teachers.objects.all()
	serializer_class = TeachersSerializers


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Teachers.objects.all()
	serializer_class = TeachersSerializers


class CategoriesListView(generics.ListCreateAPIView):
	queryset = Categories.objects.all()
	serializer_class = CategoriesSerializers


class CategoriesDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Categories.objects.all()
	serializer_class = CategoriesSerializers

class CoursesListView(generics.ListCreateAPIView):
	queryset = Courses.objects.all()
	serializer_class = CoursesSerializers


class CoursesDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Courses.objects.all()
	serializer_class = CoursesSerializers

	
class CommentListView(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerialezers


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerialezers


class ChapterListView(generics.ListCreateAPIView):
	queryset = Chapter.objects.all()
	serializer_class = ChapterSerializers


class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Chapter.objects.all()
	serializer_class = ChapterSerializers      
	