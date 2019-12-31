from django.contrib import admin

# Register your models here.
from fullstackexam.models import Room, RoomType, Rating, RatingCategory


class RoomAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Room._meta.fields if field.name != ""]


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RoomType._meta.fields if field.name != ""]


class RatingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rating._meta.fields if field.name != ""]


class RatingCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RatingCategory._meta.fields if field.name != ""]


admin.site.register(Room, RoomAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(RatingCategory, RatingCategoryAdmin)