from django.urls import path
from . import views


urlpatterns = [    
    
    path('demo/', views.index_demo, name='home-index-demo' ),
    path('', views.index, name='home-index' ),
    path('workouts/', views.w_index, name='workout-index')
]