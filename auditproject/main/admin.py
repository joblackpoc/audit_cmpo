from atexit import register
from django.contrib import admin
from .models import Document, Sectionlist
# Register your models here.

admin.site.register(Document)
admin.site.register(Sectionlist)