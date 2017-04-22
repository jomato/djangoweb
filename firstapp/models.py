from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class People(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.name


class Artical(models.Model):
    headline = models.CharField('标题', null=False,  blank=True, max_length=100)
    content = models.TextField('正文', null=True, blank=True)
    created_time = models.DateField('创建时间')
    modified_time = models.DateTimeField('修改时间')
    author = models.ForeignKey('People', verbose_name='作者', blank=True, null=True)
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.id})


class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'pk': self.id})


class Tag(models.Model):
    name = models.CharField('标签名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now_add=True)

    def __str__(self):
        return self.name























