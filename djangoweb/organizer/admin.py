from django.contrib import admin
from .models import NewsLink, Startup, Tag

#admin.site.register(NewsLink)
#admin.site.register(Startup)
#admin.site.register(Tag)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name","slug")

@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display = ("name","slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(NewsLink)
class NewsLinkAdmin(admin.ModelAdmin):
    list_display = ("title","slug")
    prepopulated_fields = {"slug": ("title",)}
