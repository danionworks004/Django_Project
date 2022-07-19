from.import views
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome),
    path('home/',include('home.urls')),
    path('about/', include('about.urls')),
    
]
urlpatterns+=staticfiles_urlpatterns()
