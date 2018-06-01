from django.contrib import admin

# Register your models here.

from .models import User, Note

admin.site.register(User)
admin.site.register(Note)