from django.contrib import admin

# Register your models here.
from .models import Timeline, Event

admin.site.register(Timeline)
admin.site.register(Event)

