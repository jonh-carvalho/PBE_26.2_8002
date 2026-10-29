from django.contrib import admin

from content_app.models import Comment, Content, Like, Playlist, Subscription, ViewHistory

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'is_public', 'upload_date')
    list_filter = ('content_type', 'is_public')
    search_fields = ('title', 'description')
    ordering = ['-upload_date']
    fieldsets = (
    ('Informações Básicas', {'fields': ('title', 'description')}),
    ('Detalhes do Arquivo', {'fields': ('file_url', 'thumbnail_url')}),
  )

# Register your models here.
admin.site.register(Content, ContentAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Playlist)
admin.site.register(Subscription)
admin.site.register(ViewHistory)
