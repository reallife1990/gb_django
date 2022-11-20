from django.contrib import admin
from mainapp.models import *

"""
list_display- отображение списка
fields - отображение для редактирования
"""


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'preamble', 'updated_at', 'deleted')
    fields = ('title', 'preamble', 'body', 'body_as_markdown', 'deleted')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cost', 'updated_at', 'deleted')
    fields = ('title', 'description', 'cost', 'deleted')


class CourseTeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'updated_at', 'deleted')
    fields = ('first_name', 'last_name', 'courses', 'deleted')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('num', 'title', 'description', 'course', 'updated_at', 'deleted')
    fields = ('num', 'title', 'description', 'course', 'deleted')


admin.site.register(News,NewsAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseTeacher, CourseTeacherAdmin)
admin.site.register(Lesson, LessonAdmin)
