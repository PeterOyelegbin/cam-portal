"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from accounts.views import loginUser, listUsers, createUser, userDetails, updateUser, deleteUser, logoutUser
from loans.views import applicationList, applicationForm, applicationDetails, applicationUpdate, applicationDelete, applicationReview


urlpatterns = [
    path("admin/", admin.site.urls),
    
    # User authentication routes
    path('accounts/login', loginUser, name='login'),
    path('accounts/logout', logoutUser, name='logout'),
    path('accounts/users', listUsers, name='users'),
    path('accounts/create', createUser, name='createUser'),
    path('accounts/users/<pk>', userDetails, name='userDetails'),
    path('accounts/update/<pk>', updateUser, name='updateUser'),
    path('accounts/delete/<pk>', deleteUser, name='deleteUser'),
    # Password reset routes
    path('accounts/reset-password', PasswordResetView.as_view(), name="password_reset"),
    path('accounts/reset-password/done', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('accounts/reset-password/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('accounts/reset-password/complete', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
    # Loan application and review routes
    path('', applicationList, name='home'),
    path('application/form', applicationForm, name='applicationForm'),
    path('application/details/<pk>', applicationDetails, name='applicationDetails'),
    path('application/update/<pk>', applicationUpdate, name='applicationUpdate'),
    path('application/delete/<pk>', applicationDelete, name='applicationDelete'),
    path('application/reviews/<pk>', applicationReview, name='applicationReview'),
]
