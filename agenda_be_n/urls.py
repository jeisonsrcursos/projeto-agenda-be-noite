
from django.contrib import admin
from django.urls import path, include

from api.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    # API V1
    path('api/v1/', include('api.urls')),
    # API V2
    path('api/v2/', include(router.urls))
]
