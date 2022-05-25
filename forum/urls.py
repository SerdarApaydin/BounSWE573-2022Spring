from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('space/<int:space_id>/forum/', views.list_forum , name= 'list_forum'),
    path('space/<int:space_id>/forum/create_post', views.post_forum , name= 'post_forum'),
    path('space/<int:space_id>/forum/<int:post_id>', views.post_detail , name= 'post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
