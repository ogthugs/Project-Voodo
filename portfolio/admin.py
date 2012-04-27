from django.contrib import admin

from portfolio.models import *

class AuthorAdmin(admin.ModelAdmin):
    fields = ('public_id', 'created_on', 'updated_on')

admin.site.register(Project)