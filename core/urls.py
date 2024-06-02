from django.urls import path

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('files/', views.file_index, name="file_index"),
    path('files/<int:pk>/', views.file_detail, name='file_detail'),
    path('files/<int:pk>/delete', views.file_delete, name='file_delete'),
    path('entities/<int:pk>/delete', views.entity_delete, name='entity_delete'),
]
