from django.contrib import admin
from .models import Paper

@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
