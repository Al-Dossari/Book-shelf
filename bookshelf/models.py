from django.db import models
from autoslug import AutoSlugField
from rest_framework.reverse import reverse


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    key = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    status_choices = [(0, "new"), (1, "reading"), (2, "finished")]
    status = models.IntegerField(choices=status_choices, default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
