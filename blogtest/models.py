from django.db import models
from django.conf import settings


class Post(models.Model):
    # related-name은 별명(alias)과 같은 맥락인가요?
    # http://stackoverflow.com/questions/22538563/django-reverse-accessors-for-foreign-keys-clashing
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user1', null=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey('Category')
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Post {}: "{}">'.format(self.pk, self.title[:8])    


class Comment(models.Model):
    """댓글 모델. 필요한 모델 필드를 추가하세요.
    """
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Category(models.Model):
    """글 갈래 모델. 필요한 모델 필드를 추가하세요.
    """
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Tag {}: "{}">'.format(self.pk, self.name)