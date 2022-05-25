from django.contrib import admin
from forum.models import Post, Answer
# Register your models here.

class AnswerAdmin(admin.TabularInline):
    model = Answer

class PostAdmin(admin.TabularInline):
    model = Post
    inlines = [AnswerAdmin]
