from django.urls import path
from . import views
import os

urlpatterns = [
    path('', views.button),
    path('takeModule/add', views.add, name='add1'),
    path('takeModule/', views.take_module_page, name ='moduleTest'),
    path('output/', views.output, name='script'),
    path('takeTMA/', views.take_tma_view, name='take_tma'),
    path('takeTMA/TMA03', views.take_tma_03, name = 'tma03'),
    path('takeModule/Module07/', views.get_module, name = 'module07'),
    path('testModule', views.take_module_question, name ='generate_question')
]
