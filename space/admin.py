from django.contrib import admin
from space.models import Space, Tag, LearningMaterials
from forum.admin import PostAdmin,AnswerAdmin
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag

class LearningMaterialsAdmin(admin.StackedInline):
    model = LearningMaterials

class SpaceAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningMaterialsAdmin, PostAdmin]


admin.site.register(Space, SpaceAdmin)
admin.site.register(LearningMaterials)
