from django.contrib import admin

from .models import Event


@admin.register(Event)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
        'created',
        'start_date',
        'start_time',
        'end_time',
        'responsible',
    )
    search_fields = ('title',)
    list_filter = ('start_date',)
    empty_value_display = '-пусто-'
