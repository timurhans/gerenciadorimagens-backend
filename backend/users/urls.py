from django.urls.conf import path
from .views import CreateUser, CreateUserByAdmin, UserLogin, ViewUsers


app_name = 'users'

urlpatterns = [
    path('', ViewUsers.as_view(), name='viewusers'),
    path('create/', CreateUser.as_view(), name='createuser'),
    path('create/admin/', CreateUserByAdmin.as_view(), name='createuserbyadmin'),
    path('login/', UserLogin.as_view(), name='userlogin')
]