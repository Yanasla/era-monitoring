from django.contrib import admin
from monitoring.models import Operator, Test

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Operator, AuthorAdmin)

class TestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Test, TestAdmin)