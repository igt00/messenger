from django.urls import path

from accounts.views import CreateUserAPIView, LoginUserAPIView, ChangePasswordAPIView, LogoutUserAPIView

urlpatterns = [
    path('register/', CreateUserAPIView.as_view(), name='register'),
    path('login/', LoginUserAPIView.as_view(), name='login'),
    path('logout/', LogoutUserAPIView.as_view(), name='logout'),
    path('change_pass/', ChangePasswordAPIView.as_view(), name='change_pass'),
]