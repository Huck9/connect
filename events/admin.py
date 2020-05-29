from django.contrib import admin
from .models import MainEvent, SmallEvent, EventRegister, EventSmallRegister

# Register your models here.

admin.site.register(MainEvent)
admin.site.register(SmallEvent)
admin.site.register(EventRegister)
admin.site.register(EventSmallRegister)