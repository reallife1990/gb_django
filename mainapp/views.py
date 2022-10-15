from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CourseslistView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocsiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

