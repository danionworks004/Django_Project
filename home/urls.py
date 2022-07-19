from multiprocessing.spawn import import_main_path
from.import views
from django.urls import path

urlpatterns = [
    path('',views.index),
]
