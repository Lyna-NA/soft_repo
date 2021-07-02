from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Book)
admin.site.register(Issue)
admin.site.register(Floor)
admin.site.register(Category)
admin.site.register(Shelf)
admin.site.register(BookPosition)
