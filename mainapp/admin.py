from django.contrib import admin

from .models import Technics, Tactics, Implementation, Title


class TacticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    search_fields = ('description',)
    list_filter = ('name',)

class TechnicsAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'description',)
    search_fields = ('description',)
    list_filter = ('name',)

# admin.site.register(Title)
# admin.site.register(Implementation)
admin.site.register(Tactics, TacticsAdmin)
admin.site.register(Technics, TechnicsAdmin)