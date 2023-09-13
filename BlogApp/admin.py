from django.contrib import admin
from BlogApp.models import *
admin.register(Blog,Comment_section,Share_blg)(admin.ModelAdmin)
# Register your models here.
