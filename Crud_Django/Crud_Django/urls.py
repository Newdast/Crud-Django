from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/', views.create_task, name='create_tasks'),
    path('tasks/<int:task_id>/', views.tasks_detail, name='tasks_detail'),
    path('tasks/<int:task_id>/complete/', views.task_complete, name='task_complete'),
    path('tasks/<int:task_id>/no/completed/', views.task_no_completed, name='task_no_completed'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
