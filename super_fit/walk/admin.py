from django.contrib import admin
from .models import Walk, TestWalk, CastomWalk

# Register your models here.
admin.site.register(Walk)
admin.site.register(TestWalk)
admin.site.register(CastomWalk)