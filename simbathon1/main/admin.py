from django.contrib import admin
from .models import Blog
from .models import Vlog

# Register your models here.
admin.site.register(Blog)
admin.site.register(Vlog)