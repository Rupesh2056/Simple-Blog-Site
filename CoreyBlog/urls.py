"""CoreyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from User import views as user_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Blog.urls")),
    path('user/', include("User.urls")),
    path('login/',auth_views.LoginView.as_view(template_name="User/Login.html"),name="user-login"),
    path('logout/',auth_views.LogoutView.as_view(),name="user-logout"),
    path('profile/',user_view.Profile,name="user-profile"),
    path('profile/edit',user_view.editProfile,name="profile-edit"),

     path('password-reset/',PasswordResetView.as_view(template_name="user/password_reset.html"),name="reset-password"),
     path('password-reset_done/',PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"),name="password_reset_done"),
     path('password-reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"),name="password_reset_confirm"),
     path('password-reset_complete/',PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"),name="password_reset_complete"),
    
    
   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
