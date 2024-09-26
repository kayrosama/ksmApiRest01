from django.contrib import admin
from apps.models import Humanos

@admin.register(Humanos)
class HumanosAdmin(admin.ModelAdmin):
    list_display = ['Nombres', 'ApeUno', 'FecReg']
    