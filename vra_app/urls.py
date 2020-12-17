from django.urls import path

from . import views

app_name = 'vra'
urlpatterns = [
    path('', views.index, name='index'),
    path('see_seguros/', views.see_seguros, name='see_seguros'),
    path('seguro/<int:seguro_id>/', views.detail, name='detail'),
    path('create_seguro/', views.create_seguro, name='create_seguro'),
    path('new_seguro/', views.new_seguro, name='new_seguro'),
    path('delete/<int:seguro_id>/', views.delete_seguro, name='delete_seguro'),
    path('confirm_delete_seguro/<int:seguro_id>/', views.confirm_delete_seguro, name='confirm_delete_seguro'),
    path('update_seguro/<int:seguro_id>', views.update_seguro, name='update_seguro'),
    path('confirm_update_seguro/<int:seguro_id>/', views.confirm_update_seguro, name='confirm_update_seguro'),

    path('new_cobertura/', views.new_cobertura, name='new_cobertura'),
    path('create_cobertura/', views.create_cobertura, name='create_cobertura'),
]