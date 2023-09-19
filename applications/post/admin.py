from django.contrib import admin

from applications.post.models import Shoes, Comment, ShoesImage


class ImageInLineAdmin(admin.TabularInline):
    model = ShoesImage
    fields = ('image',)
    max_num = 5

@admin.register(Shoes)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']
    list_filter = ['owner']
    list_fields = ['title']

    def like_count(self, obj):
        return obj.likes.filter(is_like=True).count()

admin.site.register(Comment)

