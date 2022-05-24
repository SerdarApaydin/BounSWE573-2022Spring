from django.contrib import admin
from space.models import Space, Tag, LearningMaterials
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag

class LearningMaterialsAdmin(admin.StackedInline):
    model = LearningMaterials

class SpaceAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningMaterialsAdmin]


admin.site.register(Space, SpaceAdmin)
admin.site.register(LearningMaterials)
