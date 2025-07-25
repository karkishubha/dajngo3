from django.urls import path, include
from django.contrib import admin
from display_page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display/', views.home,name="home")
]
