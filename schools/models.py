from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=64)
    actual_file = models.FileField(upload_to='files')

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str__(self):
        return self.title
