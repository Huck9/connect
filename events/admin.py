from django.contrib import admin
from .models import MainEvent, SmallEvent

# Register your models here.

admin.site.register(MainEvent)
admin.site.register(SmallEvent)
