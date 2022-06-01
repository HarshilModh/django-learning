from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(News)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Abc)

