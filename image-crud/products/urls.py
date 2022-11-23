from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('', views.index, name="/"),
    path('add-product/', views.addProduct, name="add-prod"),
    path('edit-product/<str:pk>', views.editProduct, name="edit-prod"),
    path('delete-product/<str:pk>', views.deleteProduct, name="delete-prod"),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="logout"),
]
