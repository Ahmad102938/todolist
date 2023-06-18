from django.urls import path

from .views import TaskList, TaskDetail, CreateTask, SaveTask, DeleteTask, edit, update, SignUpView, LoginView, userdetail
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('', TaskList.as_view(), name='tasks'),
    path('home/', TaskList, name='hometasks'),
    # path('search/', search, name='search'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('task/<int:id>/', TaskDetail, name='tasks'),
    path('create/', CreateTask, name='tasks'),
    path('savetask/', SaveTask, name='savetask'),
    path('delete/<int:id>/', DeleteTask, name='delete'),
    path('edit/<int:id>/', edit, name='edit'),
    path('update/<int:id>/', update, name='update'),
    path('user/', userdetail, name='userdetail'),
    path('', SignUpView, name='signup'),
    path('login/', LoginView, name='login'),
    # path('next/', Next, name='next')
    # path('task/<int:pk>/', TaskDetail.as_view(), name='tasks'),
    # path('task-create/', TaskCreate.as_view(), name='task-create'),
]
