from django.contrib import admin
from app.models import Author as AuthorModel


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'title', 'birth_date')
    list_display = ('name', 'title')
    list_filter = ('name', 'title', 'birth_date')
    search_fields = ('name', 'title', 'birth_date',)
    ordering = '-name',


# Register your models here.
admin.site.register(AuthorModel, AuthorAdmin)
