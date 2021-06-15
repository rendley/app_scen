from django.contrib import admin

from .models import Technics, Tactics, Implementation, Title, Threat


class TacticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    search_fields = ('description',)
    list_filter = ('name',)


class TechnicsAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'description',)
    search_fields = ('description',)
    list_filter = ('name',)


class ImplementationAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ThreatAdmin(admin.ModelAdmin):
    list_display = ('id','number', 'name',) 

# admin.site.register(Title)
# admin.site.register(Implementation)
admin.site.register(Tactics, TacticsAdmin)
admin.site.register(Technics, TechnicsAdmin)
admin.site.register(Implementation, ImplementationAdmin)
admin.site.register(Threat, ThreatAdmin)
