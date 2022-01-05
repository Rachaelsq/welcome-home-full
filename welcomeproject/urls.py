
# ======================================================
#PROJECT URLS include the APPNAME.urls files of each app
#=======================================================
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('journalapp.urls')),
    #path('', include('loginapp.urls')),
    #path('', include('mainapp.urls')),
]
