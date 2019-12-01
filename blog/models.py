from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author   = models.ForeignKey(User, on_delete=models.CASCADE)
    title    = models.CharField(max_length=250)
    content  = models.TextField()
    image    = models.FileField
    publish  = models.DateTimeField(default=timezone.now)
    


    def __str__(self):
        return self.title

# Database table shewing file_uploads 
class Files_Upload(models.Model):
    post   = models.ForeignKey(Post, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/%B/%d/%Y', null=True, blank=True) # For uploading Images.
    videos = models.FileField(upload_to='videos/%B/%d/%Y', null=True, blank=True) # mainly For uploading videos.


class Comment(models.Model):
    post       = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name       = models.CharField(max_length=80)
    body       = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return 'Comment {}. by {}'.format(self.body, self.name)

    class Meta:
        ordering = ['-created_on']

