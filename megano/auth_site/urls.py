from django.urls import path
from auth_site import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/password/', views.ChangePasswordView.as_view(), name='change-password'),
]
