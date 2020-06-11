
from django.contrib import admin
from django.urls import path, include

from practice import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('practice/', include('practice.urls')),
]

