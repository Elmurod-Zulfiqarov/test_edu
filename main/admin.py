from django.contrib import admin
from .models import Students, Teachers, Categories, Courses, Comment, Chapter

admin.site.register([Students, Teachers, Categories, Courses, Comment, Chapter])
