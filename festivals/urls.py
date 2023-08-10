from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_festivals, name='festivals'),
    path('<int:festival_id>/', views.festival_detail, name='festival_detail'),
    path('add/', views.add_festival, name='add_festival'),
    path('edit/<int:festival_id>/', views.edit_festival, name='edit_festival'),
    path('delete/<int:festival_id>/', views.delete_festival, name='delete_festival'),  # noqa
]
