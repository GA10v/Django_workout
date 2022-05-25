from django.urls import path
from . import views


urlpatterns = [
    path('', views.workout),
    path('<int:focus>/', views.get_wk),
    ]