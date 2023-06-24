from django.urls import path
from . import views


urlpatterns = [
    path('', views.button),
    path('output/', views.output, name='script'),
    path('takeTMA/', views.take_tma_view, name='take_tma'),
    path('takeTMA/TMA03', views.take_tma_03, name = 'tma03')
]
