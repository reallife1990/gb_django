python manage.py dumpdata mainapp.News > mainapp/fixtures/news.json
 python manage.py dumpdata приложение.модель  параметр> файл - фикстура
 --indent 2  красивый вывод в файл
 python manage.py loaddata mainapp/fixtures/news.json - загрузка

