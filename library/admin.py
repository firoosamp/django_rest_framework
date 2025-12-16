from django.contrib import admin


from library.models import Book

from library import models
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title' , 'price')

admin.site.register(models.Author)