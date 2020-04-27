from django.urls import path
from django.contrib.auth.views import *
from account import views
app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="registration/logged_out.html"), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name="registration/password_change_form.html"), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name="registration/password_change_form.html"), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name="registration/password_reset_form.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

urlpatterns += [
    path('register/', views.register, name = 'register_main')

]