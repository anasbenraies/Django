from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default="fallback.png",blank=True)

    def __str__(self):
        return self.title
