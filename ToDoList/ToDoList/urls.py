"""ToDoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# 메커니즘 : 사용자가 ''에 접근했을 때 기본 화면 ToDoList를 보여줘야함.
# ToDoList 화면 처리를 위해 my_to_do_app이라는 application 만듬.
# ToDoList의 urls.py의 역할은 my_to_do_apps의 urls.py에게 처리를 넘겨주는 것.

urlpatterns = [
    path('admin/', admin.site.urls),  # 실제로는 'http://127.0.0.1:8000/admin'에 접근했을 때 admin.site.urls로 접근해라.
    path('', include('my_to_do_app.urls'))
]
