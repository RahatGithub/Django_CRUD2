from django.contrib import admin
from .models import Player

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'country', 'franchise')