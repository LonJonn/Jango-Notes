from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'dateCreated',
                    'dateDue', 'group', 'colour')
    list_filter = ('owner', 'group', 'colour', 'dateCreated')
    fieldsets = (
        (None, {
            'fields': ('owner', 'title', 'description')
        }),
        ('Filter', {
            'fields': ('colour', 'group')
        }),
        ('Reminder', {
            'fields': ['dateDue']
        })
    )


admin.site.register(Note, NoteAdmin)
