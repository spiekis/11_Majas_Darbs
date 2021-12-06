"""django_users URL Configuration

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
from django.urls import path

import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users.views.get_users),
    path('add-user', users.views.add_user),
    path('add-user-csv', users.views.add_user_csv),
    path('filter-users/user', users.views.filtred_users_by_username),
    path('user/<int:user_id>', users.views.get_user, name='get-user')
]
