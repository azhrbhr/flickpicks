from django.urls import path
from accounts.views import RegisterView, LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordChangeView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', PasswordResetView.as_view(
        html_email_template_name='registration/password_reset_email.html'), name='password_reset'),
]
