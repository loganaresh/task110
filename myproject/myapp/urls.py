from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, activate

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    
]
