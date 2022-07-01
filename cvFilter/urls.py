"""cvFilter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from pages import views as mainV 
from applicant import views as dashboard 

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', mainV.landing_page),
    # path('apply/',mainV.apply),
    path('apply/',dashboard.apply),
    path('dashboard/',dashboard.dashboard),
    path('list/',dashboard.index),
    path('admin/', admin.site.urls),
    path('indexing', dashboard.indexing, name='indexing'),
    path('search', dashboard.search)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
