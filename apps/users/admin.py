from django.contrib import admin
from .models import Organisation, User

# Register your models here.
admin.site.register(User)
admin.site.register(Organisation)
