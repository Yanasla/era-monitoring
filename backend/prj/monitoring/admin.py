from django.contrib import admin
from monitoring.models import Operator

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Operator, AuthorAdmin)
