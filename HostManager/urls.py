"""HostManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from host.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
<<<<<<< HEAD
=======
    url(r'^user', user),
    url(r'^house', house),
    url(r'^selectuser', selectuser),
    url(r'^delteuser/(\d+)', delteuser),
    url(r'^updateuser/(\d+)', updateuser),
    url(r'^selecthouse', selecthouse),
    url(r'^deltehouse/(\d+)', deltehouse),
    url(r'^updatehouse/(\d+)', updatehouse),
    url(r'^fileload', fileload),
    url(r'^createcode', createcode),
    url(r'^code', code),
    url(r'^additem', additem),
    url(r'^addhouse', addhouse),
    url(r'^checkland', checkland),


>>>>>>> 自动化测试脚本2018/07/06 17:38:42 更新
]
