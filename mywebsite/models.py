from django.conf import settings
from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.FileField(upload_to='mywebsite/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name='post_categories', null=True, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_likes')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=150)
    body = models.TextField()
    comment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)
