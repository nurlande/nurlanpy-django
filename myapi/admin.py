from django.contrib import admin
from .models import Registration
from .models import User

# Register your models here.

admin.site.register(Registration)
admin.site.register(User)
