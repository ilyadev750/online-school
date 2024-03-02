from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('', include('users.urls')),
    path('', include('lessons.urls')),
    path('api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    path("__debug__/", include("debug_toolbar.urls")),
]
