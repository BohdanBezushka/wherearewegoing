from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_festivals, name='festivals'),
    path('<festival_id>', views.festival_detail, name='festival_detail'),
]
