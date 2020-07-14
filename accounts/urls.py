from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    # Login
    path('login', views.login, name='login'),

    # Registration
    path('registration', views.register, name='registration'),

    # Logout
    path('logout', views.logout, name='logout'),

    # Password change
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='authentication/reset_password/password_change_form.html'
    ), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='authentication/reset_password/password_change_done.html'
    ), name='password_change_done'),

    # Reset password urls
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='authentication/reset_password/password_reset_form.html'
         ), name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='authentication/reset_password/password_reset_done.html'
         ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='authentication/reset_password/password_reset_confirm.html'
         ), name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='authentication/reset_password/password_reset_complete.html'
         ), name='password_reset_complete'),
]
