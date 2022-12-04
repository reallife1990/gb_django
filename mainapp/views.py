from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, DetailView, DeleteView, CreateView, ListView
from django.http import HttpResponse, JsonResponse
from datetime import datetime

#3:10 видео дз

from mainapp.forms import CourseFeedbackForm
from mainapp.models import News, Course, Lesson, CourseTeacher, CourseFeedback


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['contacts'] = [
            {
                'map': "https://yandex.ru/map-widget/v1/-/CCUAZHcrhA",
                'city': 'Санкт‑Петербург',
                'phone':'+7-999-11-11111',
                'email': 'geeklab@spb.ru',
                'address':'территория Петропавловская крепость, 3Ж'
            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city': 'Казань',
                'phone': '+7-999-22-22222',
                'email': 'geeklab@kz.ru',
                'address': 'территория Кремль, 11, Казань, Республика Татарстан, Россия'
            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city': 'Москва',
                'phone':'+7-999-33-3333',
                'email': 'geeklab@msk.ru',
                'address':'Красная площадь, 7, Москва, Россия'
            },
        ]

        return context_data


class CoursesListView(ListView):
    template_name = 'mainapp/courses_list.html'
    model = Course


class DocsiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsListView(ListView):
    model = News
    # template_name = 'mainapp/news_list.html'
    # не нужен, если мия шаблона совпадает с именем модели и имеет постфикс типа вьюхи
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

# class NewsView(TemplateView):
#     template_name = 'mainapp/news_list.html'
#
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         context_data['news_list'] = News.objects.filter(deleted=False)
#         return context_data


class NewsDetailView(DetailView):
    model = News


class NewsCreateView(PermissionRequiredMixin,CreateView):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('mainapp:news')
    permission_required = ('mainapp.add_news',)


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('mainapp:news')
    permission_required = ('mainapp.change_news',)


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = News

    success_url = reverse_lazy('mainapp:news')
    permission_required = ('mainapp.delete_news',)


class CourseDetailView(TemplateView):
    template_name = 'mainapp/courses_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['course_object'] = get_object_or_404(Course, pk=self.kwargs.get('pk'))
        context_data['lessons'] = Lesson.objects.filter(course=context_data['course_object'])
        context_data['teacher'] = CourseTeacher.objects.filter(courses=context_data['course_object'])
        context_data['feedback_list'] = CourseFeedback.objects.filter(course=context_data['course_object'])

        if self.request.user.is_authenticated:
            context_data['feedback_form'] = CourseFeedbackForm(course=context_data['course_object'],
                                                               user=self.request.user)


        return context_data


class CourseFeedbackCreateView(CreateView):
    model = CourseFeedback
    form_class = CourseFeedbackForm

    def form_valid(self, form):
        self.object =form.save()
        rendered_template = render_to_string('mainapp/includes/feedback_card.html',
                                             context={'item' : self.object})
        return JsonResponse({'card':rendered_template})

# class NewsDetail(TemplateView):
#     template_name = 'mainapp/news_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         context_data['object'] = get_object_or_404(News, pk=self.kwargs.get('pk'))
#         return context_data