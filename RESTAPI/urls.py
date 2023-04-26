
from django.contrib import admin
from django.urls import path , include
from API import urls   # import urls.py file form API Application 
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/" , include('API.urls'))  # inculd urls.py file form API Application 
]
