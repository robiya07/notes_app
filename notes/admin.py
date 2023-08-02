from django.contrib import admin

from notes.models import NoteModel


# Register your models here.
@admin.register(NoteModel)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title', )
    search_fields = ('title',)
