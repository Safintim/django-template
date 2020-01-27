from django.contrib import admin

from app import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'id',
        'phone',
    )

    search_fields = (
        'phone',
    )
