from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='index'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('view/<int:key>', views.viewRecord, name='record'),
    path('delete/<int:key>', views.deleteRecord, name='delete'),
    path('add/', views.addRecord, name='add'),
    path('update/<int:key>', views.updateRecord, name='update'),
]
