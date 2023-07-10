
from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('add_item/', views.add_item, name='add_item'),
    path('menu_detail/<int:id>', views.menu_detail, name='menu_detail'),
    path('item_update/<int:id>', views.item_update, name='item_update'),
]
