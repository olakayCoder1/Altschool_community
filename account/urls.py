from django.urls import path
from . import views



urlpatterns = [ 
    path('', views.AccountView.as_view(), name="account"),  
    path('update', views.account_profile_update, name="account_profile_update"),  
    path('login', views.LoginView.as_view() , name='login'),  
    path('logout', views.logout_view , name='logout'),  
    path('register', views.RegisterView.as_view() , name='register'),  
    path('forget-password', views.ForgetPasswordView.as_view() , name='forget-password'),  
    path('forget-password/<str:token>/<str:uuidb64>/confirm', views.ForgetPasswordConfirm.as_view(), name='forget_password-confirm'),

]