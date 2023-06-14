from django.urls import path

from .views import TaskList, TaskDetail, CreateTask, SaveTask, DeleteTask, edit, update, SignUpView, LoginView

urlpatterns = [
    # path('', TaskList.as_view(), name='tasks'),
    path('home/', TaskList, name='hometasks'),
    path('task/<int:id>/', TaskDetail, name='tasks'),
    path('create/', CreateTask, name='tasks'),
    path('savetask/', SaveTask, name='savetask'),
    path('delete/<int:id>/', DeleteTask, name='delete'),
    path('edit/<int:id>/', edit, name='edit'),
    path('update/<int:id>/', update, name='update'),
    path('', SignUpView, name='signup'),
    path('login/', LoginView, name='login')
    # path('task/<int:pk>/', TaskDetail.as_view(), name='tasks'),
    # path('task-create/', TaskCreate.as_view(), name='task-create'),
]
