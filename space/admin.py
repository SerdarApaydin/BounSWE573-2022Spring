from django.contrib import admin
from space.models import Space, Tag, LearningMaterialVideos
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag

class LearningMaterialVideosAdmin(admin.StackedInline):
    model = LearningMaterialVideos

class SpaceAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningMaterialVideosAdmin]


admin.site.register(Space, SpaceAdmin)
admin.site.register(LearningMaterialVideos)
