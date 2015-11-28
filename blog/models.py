from django.db import models
from django.conf import settings

# from django.contrib.auth.models import AbstractUser
# 이렇게 쓰지말고 AbstractUser를 쓰세요
# class Profile(User):
#     pass


# class BasePost(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     category = models.ForeignKey('Category')
#     tags = models.ManyToManyField('Tag', blank=True)
    
#     class Meta:
#         abstract = True

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey('Category')
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Post {}: "{}">'.format(self.pk, self.title[:8])


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Category {}:"{}">'.format(self.pk, self.name)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Comment {}>'.format(self.pk)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Tag {}: "{}">'.format(self.pk, self.name)