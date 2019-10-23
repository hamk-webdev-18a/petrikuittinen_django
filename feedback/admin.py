from django.contrib import admin

from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('good', 'bad', 'ideas')
    list_filter = ['date']
    search_fields = ['good', 'bad', 'ideas']
    
admin.site.register(Feedback, FeedbackAdmin)
                
