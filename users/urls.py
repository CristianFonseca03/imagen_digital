from django.urls import path
from users import views
from users.views import UserDetailView

app_name='users'
urlpatterns = [
    path(route='login/', view=views.login_view, name='login'),
    path(route='logout/', view=views.logout_view, name='logout'),
    path(route='<str:username>/', view=UserDetailView.as_view(), name='detail'),
]
