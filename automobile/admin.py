from django.contrib import admin

from automobile import models


@admin.register(models.Auto)
class AutoAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


