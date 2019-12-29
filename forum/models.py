import uuid
from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.first_name:
            self.first_name = self.user.first_name
        if not self.last_name:
            self.last_name = self.user.last_name
        super().save(*args, **kwargs)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.pk}: {self.full_name}'

class Tag(models.Model):
    text = models.CharField(max_length=20)


class Article(models.Model):
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, null=True)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=99, decimal_places=2)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ManyToManyField(Book, through='OrderLine')

    def __str__(self):
        return f'{self.user.username}\'s Basket #{self.pk}'

    @property
    def total(self):
        lines = self.Orderlines.select_related('book').all()
        total = 0
        for line in lines:
            total += line.total
        return total

class OrderLine(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orderlines')
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='orderlines')
    quantity = models.IntegerField()

    def __ste__(self):
        return f'{self.pk}({self.book.title}): Basket: {self.basket.pk}'

    @property
    def total(self):
        return self.book.price * self.quantity

# class UselessModel(models.Model):
#     LANGUAGE_CHOICES = [
#         ('ru', 'Russian'),
#         ('en', 'English'),
#         ('by', 'Belarussian'),
#     ]

#     language = models.CharField(
#         choices=LANGUAGE_CHOICES,
#         max_length=2,
#         default='ru',
#         help_text='Field for chosing language',
#     )

# class Model2(models.Model):
#     new_id = models.AutoField(primary_key=True)
#     some_name = models.BooleanField(default=False, null=True, blank=True)
#     some_attr = models.CharField(max_length=30,  null=True, blank=True)
#     text = models.TextField(max_length=1000, null=True, blank=True)
#     number = models.IntegerField( null=True, blank=True)
#     flo = models.FloatField( null=True, blank=True)
#     dec = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     email = models.EmailField( null=True, blank=True)
#     birthday = models.DateField(null=True, blank=True)
#     url = models.URLField(max_length=300, null=True, blank=True)


# class Model3(models.Model):
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     file_f = models.FileField(upload_to='uploads/', null=True, blank=True)
#     image_f = models.ImageField(upload_to='images/', null=True, blank=True)
