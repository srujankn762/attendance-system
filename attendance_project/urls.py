from django.contrib import admin
from django.urls import path, include

from attendance.views import healthz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('attendance.urls')),
    path('healthz', healthz),

]
