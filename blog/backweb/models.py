from django.db import models


class User(models.Model):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class ArticleType(models.Model):
    t_name = models.CharField(max_length=30, unique=True, null=True)
    f_type = models.ForeignKey('self', null=True)

    class Meta:
        db_table = 'articleType'


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    describe = models.CharField(max_length=150, null=True)
    content = models.TextField(null=True)
    tags = models.CharField(null=True, max_length=20)
    icon = models.ImageField(upload_to='backweb', null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    modify_time = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(User, null=True)
    type = models.ForeignKey(ArticleType, default=1)

    class Meta:
        db_table = 'article'
