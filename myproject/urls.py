from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ai/', include('ai_app.urls')),
    path('', lambda request: redirect('ai_index')),
    path('accounts/', include('django.contrib.auth.urls')),  # Add Django's auth URLs
]
