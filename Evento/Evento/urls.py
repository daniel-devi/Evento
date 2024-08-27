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
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Accounts.views import CreateUserView
from Core.views import HomeView

# Define URL patterns for the project
urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),
    
    # JWT token endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    
    # Django Rest Framework authentication URLs
    path("api-auth/", include("rest_framework.urls")),
    
    # User registration endpoint
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    
    # Djoser authentication URLs
    path('auth/', include('djoser.urls')),
    
    # Include URLs from the Core app
    path('Core-Api/', include('Core.urls')),
    
    # Include URLs from the Accounts app
    path('Accounts-Api/', include('Accounts.urls')),
    
    # Home page
    path('', HomeView, name="home"),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)