from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name= 'home'),
    path('space/<int:space_id>', views.spacePage , name= 'spacePage'),
    path('space/<int:space_id>/upload', views.uploadContent , name= 'uploadContent'),
    path('create_space', views.create_space, name="create_space"),
    path('space/<int:space_id>/<int:material_id>', views.material_detail, name="material_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
