from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateField(auto_now_add=True)

    post = models.ForeignKey('firstapp.Artical')#注意直接从firstapp导入Artical会报错

    def __str__(self):
        return self.text[:20]
