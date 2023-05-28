"""ShowSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from ShowSite import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'application$', views.application, name='application'),
    url(r'application_post$', views.application_post, name='application_post'),
    url(r'test', views.test, name='test'),
    url(r'train$', views.train, name='train'),
    url(r'add_ajax', views.add_ajax, name='add_ajax'),
    url(r'^$', views.home, name='home'),
    url(r'about_us$', views.about_us, name='about_us'),
]
