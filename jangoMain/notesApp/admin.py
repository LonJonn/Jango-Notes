from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):  #specify how note model appears in the admin page
    list_display = ('title', 'owner', 'dateCreated',    #order to display
                    'dateDue', 'group', 'colour')
    list_filter = ('owner', 'group', 'colour', 'dateCreated')   #filter options for admin
    fieldsets = (   #field sets
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


admin.site.register(Note, NoteAdmin)    #register note app to admin site
