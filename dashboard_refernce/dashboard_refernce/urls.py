from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Growth_dashboard/', include('Growth_dashboard.urls')),
    path('', include('accounts.urls')),

]
