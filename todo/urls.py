from django.urls import path
from . import views
app_name = "todos"

urlpatterns = [
    path("", views.list, name="list"),
    path('create/', views.create, name='create'),
    path('<int:id>/update', views.update, name='update'),
    path("<int:id>/",views.detail, name="detail"),

    ]