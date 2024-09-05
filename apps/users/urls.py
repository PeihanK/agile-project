from django.urls import path
from apps.users.views.user_views import *


urlpatterns = [
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # конкретный пользователь
    path('users/', UserListGenericView.as_view(), name='user-list'),  # список пользователей
    path('register/', RegisterUserGenericView.as_view(), name='user-register'),  # регистрация пользователя

]
