from django.contrib import admin

from .models import Setup, Specification

class SpecificationInlineAdmin(admin.StackedInline):
    model = Specification
    extra = 0

class SetupAdmin(admin.ModelAdmin):

    model = Setup

    inlines = [SpecificationInlineAdmin, ]

admin.site.register(Setup, SetupAdmin)
