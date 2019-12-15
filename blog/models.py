from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author   = models.ForeignKey(User, on_delete=models.CASCADE)
    title    = models.CharField(max_length=250)
    content  = models.TextField()
    publish  = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')


class Comment(models.Model):
    post       = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name       = models.CharField(max_length=80)
    body       = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return 'Comment {}. by {}'.format(self.body, self.name)

    class Meta:
        ordering = ['-created_on']

