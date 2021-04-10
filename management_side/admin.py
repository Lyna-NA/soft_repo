from django.contrib import admin

# Register your models here.

from .models import Member,Book,Issue,Tag

admin.site.register(Member)
admin.site.register(Book)
admin.site.register(Issue)
admin.site.register(Tag)