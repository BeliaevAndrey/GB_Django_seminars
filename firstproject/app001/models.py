from django.db import models
from datetime import datetime as dt


class CoinPlay(models.Model):

    # throws = []

    side = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)

    # @staticmethod
    # def get_throws(amount):
    #     obverse_cnt = 0
    #     reverse_cnt = 0
    #     for item in CoinPlay.throws[-amount:]:
    #         if item[1] == 'obverse':
    #             obverse_cnt += 1
    #         else:
    #             reverse_cnt += 1
    #     return {'obverse': obverse_cnt, 'reverse': reverse_cnt, }

    @staticmethod
    def add_throw(value):
        sides = ('obverse', 'reverse')
        # CoinPlay.throws.append((dt.now(), sides[value]))
        return {'time': dt.now(), 'side': sides[value]}

    def __str__(self):
        return f'{self.side} {self.time}'


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    biography = models.TextField()
    birthday = models.DateField()

    def get_fullname(self):
        return f'{self.name} {self.surname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    publication_date = models.DateField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {self.published} {self.publication_date}'


"""
1.  CharField - поле для хранения строковых данных. Параметры:
    max_length (максимальная длина строки), blank (может ли поле быть
    пустым), null (может ли поле содержать значение Null), default (значение
    по умолчанию).

2.  IntegerField - поле для хранения целочисленных данных. Параметры:
    blank, null, default.

3.  TextField - поле для хранения текстовых данных большой длины.
    Параметры: blank, null, default.

4.  BooleanField - поле для хранения логических значений (True/False).
    Параметры: blank, null, default.

5.  DateField - поле для хранения даты. Параметры: auto_now
    (автоматически устанавливать текущую дату при создании объекта),
    auto_now_add (автоматически устанавливать текущую дату при
    добавлении объекта в базу данных), blank, null, default.

6.  DateTimeField - поле для хранения даты и времени. Параметры:
    auto_now, auto_now_add, blank, null, default.

7.  ForeignKey - поле для связи с другой моделью. Параметры: to (имя
    модели, с которой устанавливается связь), on_delete (действие при
    удалении связанного объекта), related_name (имя обратной связи).

8.  ManyToManyField - поле для связи с другой моделью в отношении
    "многие-ко-многим". Параметры: to, related_name.

9.  DecimalField - поле для хранения десятичных чисел. Параметры:
    max_digits (максимальное количество цифр), decimal_places
    (количество знаков после запятой), blank, null, default.

10. EmailField - поле для хранения электронной почты. Параметры:
    max_length, blank, null, default.
"""
