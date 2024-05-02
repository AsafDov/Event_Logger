"""
URL configuration for EventLogger_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from EventLogger import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    #path('<event>/', views.handleEventClick),
    path('api/listEntries/<str:event_id>', views.listEntries),
    path('api/listEvents/', views.listEvents),
    path('api/addEntry/', views.addEntry),
    path('api/event/<str:event>/', views.getEntries),
    path('api/event/<str:event>/<str:id>/', views.getEntry),
    path('api/deleteEntry/', views.deleteEntry),
    path('api/loadEvents/', views.loadEvents),
    path('api/exportCSV/<str:model_name>/', views.export_data_to_csv, name="exportCSV"),

]
