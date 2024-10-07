"""
URL configuration for lab2_project project.

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
# lab2_project/urls.py
# lab2_project/urls.py
from django.contrib import admin
from django.urls import path, include
from lab2.views import home, analyze_sentiment  # Đảm bảo bạn đã import hàm analyze_sentiment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Đường dẫn cho trang chính
    path('', include('lab2.urls')),
    path('analyze_sentiment/', analyze_sentiment, name='analyze_sentiment'),  # Đường dẫn cho phân tích tâm trạng
]




