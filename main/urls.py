from django.urls import path
from . import views
urlpatterns = [
    path('users/signup/', views.StudentSignup.as_view(), name='student_signup'),
    path('users/teacher-signup/', views.TeacherSignup.as_view(), name='teacher_signup'),
    path('users/login/', views.login.as_view(), name="login"),
    path('users/admin-dashboard/', views.AdminDashboard.as_view(), name="admin_dashboard"),
    path('users/teacher-dashboard/', views.TeacherDashboard.as_view(), name="teacher_dashboard"),
    path('users/student-dashboard/', views.StudentDashboard.as_view(), name="student_dashboard"),
    path('users/profile/', views.Profile.as_view(), name="profile"),
    path('all-courses/', views.CourseList.as_view(), name="course_list"),
    path('detail/<int:pk>/', views.CourseDetail.as_view(), name="course_detail"),

    # this is for test API
    path('student', views.StudentListView.as_view()),
    path('student/<int:pk>/', views.StudentDetailView.as_view()),
    path('teachers', views.TeacherListView.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetailView.as_view()),
    path('courses', views.CoursesListView.as_view()),
    path('course/<int:pk>/', views.CoursesDetailView.as_view()),
    path('categories', views.CategoriesListView.as_view()),
    path('category/<int:pk>/', views.CategoriesDetailView.as_view()),
    # path('comments', views.CommentListView.as_view()),
    # path('comment/<int:pk>/', views.CommentDetailView.as_view()),
    # path('chapters', views.ChapterListView.as_view()),
    # path('chapter/<int:pk>/', views.ChapterDetailView.as_view()),
]
