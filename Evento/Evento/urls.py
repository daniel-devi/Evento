"""
URL configuration for Evento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static # For Static Files Showing
from django.conf import settings
# Restframework
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # Restframework Authentication
# Accounts
from Accounts.views import CreateUserView
# Cores
from Core.views import HomeView

# URLS 
urlpatterns = [
    path('admin/', admin.site.urls), path("api/token/", TokenObtainPairView.as_view(), name="get_token"), # URL for Token Page
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"), # URL FOR Token Refresh 
    path("api-auth/", include("rest_framework.urls")), # URLS for Authentication 
    path("api/user/register/", CreateUserView.as_view(), name="register"), # User Registration
    path('auth/', include('djoser.urls')), # URL For BASIC User Authentication
    # Core App Url Path
    path('Core-Api/', include('Core.urls')),
    # Accounts App Url Path
    path('Accounts-Api/', include('Accounts.urls')),
    path('',HomeView.as_view(), name="home"), # Home Page
]
# URLPATTERNS FOR OPENING STATIC FILES AND MEDIA
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)