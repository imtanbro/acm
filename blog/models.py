from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from PIL import Image
STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    cover = models.ImageField(upload_to='blog-img')
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    categories = models.CharField(max_length=100, default='uncategorized')

    def __str__(self):
        return self.title
    def save(self, **kwargs):
        super().save()

        img = Image.open(self.cover.path)

        if img.height > 756 or img.width > 504:
            output_size = (756,504)
            img.thumbnail(output_size)
            img.save(self.cover.path)
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Updates(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
class upcomingEvents(models.Model):
    EventName = models.CharField(max_length=100)
    details = models.CharField(max_length=300, null=True)
    date = models.DateTimeField(null=True)
    coOrdinatorSpeaker = models.CharField(max_length=100)
    def __str__(self):
        return self.EventName

class pastEvents(models.Model):
    EventName = models.CharField(max_length=100)
    details = models.CharField(max_length=300, null=True)
    date = models.DateTimeField(null=True)
    coOrdinatorSpeaker = models.CharField(max_length=100)

    def __str__(self):
        return self.EventName

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
