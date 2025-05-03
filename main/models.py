from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    datetime = models.DateTimeField()
    text = models.TextField()
    foto = models.ImageField(upload_to='')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def  get_absolute_url(self):
        return f'/book-card/{self.id}/'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = "Книги"

    def __str__(self):
        return f'Книга: {self.title}'

