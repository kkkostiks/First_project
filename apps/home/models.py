from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Books(models.Model):
    title = models.CharField()
    author = models.CharField()
    publishing_house = models.CharField()
    language = models.CharField()
    count_pages = models.IntegerField()
    publish_year = models.IntegerField()
    year = models.IntegerField()
    datetime = models.DateTimeField()
    text = models.TextField()
    foto = models.ImageField(upload_to='book-foto')
    file = models.FileField(upload_to='book-file')


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def  get_absolute_url(self):
        return f'/book-card/{self.id}/'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = "Книги"

    def __str__(self):
        return f'Книга: {self.title}'

