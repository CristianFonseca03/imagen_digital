from django.urls import path
from users import views
from users.views import UserDetailView, HomeView, UsersListView, UserDeleteView, UserUpdateView

app_name = 'users'
urlpatterns = [
    path(route='', view=HomeView.as_view(), name='home'),
    path(route='login/', view=views.login_view, name='login'),
    path(route='signup/', view=views.signup_view, name='signup'),
    path(route='logout/', view=views.logout_view, name='logout'),
    path(route='find/<str:username>/', view=UserDetailView.as_view(), name='detail'),
    path(route='list-users/', view=UsersListView.as_view(), name='list-users'),
    path(route='delete/<str:username>/', view=UserDeleteView.as_view(), name='delete'),
    path(route='update/<str:username>/', view=UserUpdateView.as_view(), name='update'),
    path(route='changePassword/<username>/', view=views.change_password_view, name='changePassword'),
]
