from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # root points to core
    path('alevel/', include('alevel.urls')),  # can be created later
    path('olevel/', include('olevel.urls')),  # can be created later
]
