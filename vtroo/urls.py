"""vtroo URL Configuration

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
from django.urls import path,include
from vapp import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample', views.sample , name="sample"),
    path('register', views.register , name="register"),
    path('login', views.login , name="login"),
    path('logo', views.logout , name="logo"),
    path('update/<str:id>', views.update , name="update"),
    path('view/<str:id>', views.view , name="view"),
    path('check', views.check,name="check"),
    path('checkemail', views.checkemail,name="checkemail"),
    path('checkphone', views.checkphone,name="checkphone"),
    path('checkpwd', views.checkpwd,name="checkpwd"),
    path('checkform', views.checkform,name="checkform"),
    path('adminlogin', views.adminlogin, name="adminlogin"),
    path('adminview/<str:id>', views.adminview , name="adminview"),
    path('adminupdate/<str:id>', views.adminupdate , name="adminupdate"),
    path('adminlogo', views.adminlogout , name="adminlogo"),
    path('adminsample', views.adminsample , name="adminsample"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )


