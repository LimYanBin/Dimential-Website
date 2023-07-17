from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from assignment import settings

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('signupPage/', views.signupPage, name='signupPage'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),

    #profile

    path("password_reset/", 
         auth_views.PasswordResetView.as_view(template_name="password_reset.html", 
         from_email = settings.EMAIL_HOST_USER,
         html_email_template_name = "reset_email.html",
         subject_template_name = "reset_subject.txt",
         ),
         name="password_reset"),

    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="reset_done.html"),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name="reset_complete.html"),
        name="password_reset_complete",
    ),

]