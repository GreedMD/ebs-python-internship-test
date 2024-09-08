from django.contrib import admin

from apps.blog.models import Blog, Category, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "enabled")
    list_filter = ("enabled",)

    def enabled(self, obj):
        if obj.enabled:
            return "Enabled"
        else:
            return "Disabled"

    enabled.boolean = True
    enabled.short_description = "Status"


class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "blog", "created_at")
    list_filter = ("created_at",)
    search_fields = ("text", "blog__title")


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
