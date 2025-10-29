from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Importa ELS DOS models
from .models import Question, Choice

# Registra ELS DOS models
admin.site.register(Question)
admin.site.register(Choice)
