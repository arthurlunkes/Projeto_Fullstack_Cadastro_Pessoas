from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ..clientes.models import Cliente

urlpatterns = [
    path('admin/', admin.site.urls),
]
