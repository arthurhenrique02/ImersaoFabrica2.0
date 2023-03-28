from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # adicionar path para urls do coreApp
    path('principal/', include('apps.coreApp.urls'))
]
