from django.contrib import admin

from apps.blog.models import Blog, Category, Comments


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "get_status")

    def get_status(self, obj):
        if obj.enabled:
            return "Enabled"
        else:
            return "Disabled"

    get_status.short_description = "Status"


class CommentInLine(admin.TabularInline):
    model = Comments
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]
    list_display = ("title", "get_status")

    def get_status(self, obj):
        if obj.enabled:
            return "Enabled"
        else:
            return "Disabled"

    get_status.short_description = "Status"


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Comments)
