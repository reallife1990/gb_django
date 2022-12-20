from django.contrib import admin
from mainapp.models import *

"""
list_display- отображение списка
fields - отображение для редактирования
list_per_page - пагинация 
list_filter - поля для фильтрации
search_fields -  поля по которым будет поиск
actions= (действие)
    def действие(self, request, queryset):
        queryset.update(что сделать)
    действие.short_description =  название действия в меню
"""


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'preamble', 'updated_at', 'deleted')
    fields = ('title', 'preamble', 'body', 'body_as_markdown', 'deleted')
    search_fields = ["title", "preamble", "body"]
    list_filter = ["updated_at"]
    actions = ['deletenews']

    def deletenews(self, request, queryset):
        queryset.update(deleted=True)
    deletenews.short_description = 'Пометить как удалённые'



class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cost', 'updated_at', 'deleted','cover','updated_at')
    fields = ('title', 'description', 'cost', 'deleted', 'cover', 'description_as_markdown')


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
