from django.contrib import admin
from .models import GuestbookEntry

@admin.register(GuestbookEntry)
class GuestbookEntryAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_email', 'entry_text', 'created_at', 'updated_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('author_name', 'author_email', 'entry_text')
