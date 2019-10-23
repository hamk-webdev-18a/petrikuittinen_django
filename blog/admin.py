from django.contrib import admin
from .models import Blog, Author, Entry, Comment

# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 2

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['blog', 'headline', 'authors', 'body_text']}),
    ]
    inlines = [CommentInline]
    readonly_fields = ('pub_date', 'mod_date')
    list_display = ('blog', 'headline', 'pub_date', 'mod_date')    
    list_filter = ['pub_date']
    search_fields = ['headline', 'body_text']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('entry', 'text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['text']
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline')
    search_fields = ['name']
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ['name', 'email']

admin.site.register(Entry, EntryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
