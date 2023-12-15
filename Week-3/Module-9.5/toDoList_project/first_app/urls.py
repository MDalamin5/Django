from django.urls import path
from . import views


urlpatterns = [
    path('', views.MyTemplateHomeView.as_view(), name='homepage'),
    path('store_task/', views.store_task, name='store_task'),
    path('show_tasks/', views.show_tasks, name='show_tasks'),
    path('edit_task/<int:pk>', views.TaskUpdateView.as_view(), name='edit_task'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
    path('complete_task/<int:id>', views.complete_tasks, name='completed_tasks'),
    path('comp_tasks/', views.show_com_tasks, name='com_task'),
]
