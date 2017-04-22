from django.contrib import admin
from firstapp.models import People, Artical, Category, Tag

# Register your models here.


class ArticalAdmin(admin.ModelAdmin):
    list_display = ['headline', 'created_time', 'modified_time', 'author', 'category']

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


admin.site.register(People)
admin.site.register(Artical, ArticalAdmin)
admin.site.register(Category)
admin.site.register(Tag)