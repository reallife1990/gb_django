from django.db import models

NULLABLE = {'blank': True, 'null': True }


class BasicData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    # создание абстрактного класса, все поля этого класса добавятся в модели-дочери при
    # наследовании

    class Meta:
        abstract = True


class News(BasicData):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    preamble = models.CharField(max_length=256, verbose_name='Вступление')

    body = models.TextField(verbose_name='Содержание')
    body_as_markdown = models.BooleanField(default=False,verbose_name="Разметка")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Course(BasicData):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.CharField(max_length=256, verbose_name='Описание')
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(BasicData):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    num = models.PositiveIntegerField(default=0, verbose_name='Номер урока')

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.CharField(max_length=256, verbose_name='Описание')

    def __str__(self):
        return f'Урок{self.num} - {self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class CourseTeacher(BasicData):
    courses = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=150, verbose_name='Имя', blank=False)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
