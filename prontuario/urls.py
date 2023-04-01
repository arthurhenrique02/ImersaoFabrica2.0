from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # adicionar accounts url (padrao do django)
    path('accounts/', include('django.contrib.auth.urls')),

]
