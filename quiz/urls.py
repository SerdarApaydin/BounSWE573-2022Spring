from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('space/<int:space_id>/quizes/', views.list_quizes , name= 'list_quizes'),
    path('space/<int:space_id>/quizes/create_quiz', views.create_quiz , name= 'create_quiz'),
    path('space/<int:space_id>/quizes/<int:quiz_id>', views.quiz_detail , name= 'quiz_detail'),
    path('space/<int:space_id>/quizes/<int:quiz_id>/create_question', views.create_question , name= 'create_question'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
