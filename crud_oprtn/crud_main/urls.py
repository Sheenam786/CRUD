from django.urls import path
from crud_main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show/', views.show_data, name='show_data'),
    path('edit/<int:id>/', views.edit_btn, name='edit_btn'),
    path('delete/<int:id>/', views.delete_btn, name='delete_btn'),
    path('register/', views.register, name='register'),
    path('loginn/', views.loginn, name='loginn'),
    path('logout/', views.logoutpage, name='logoutpage'),
]


