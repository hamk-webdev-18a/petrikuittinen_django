from django.contrib import admin
from .models import Dictionary

class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('word', 'definition')
    search_fields = ['word', 'definition']

admin.site.register(Dictionary, DictionaryAdmin)
            
