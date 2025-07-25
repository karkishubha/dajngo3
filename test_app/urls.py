from django.urls import path, include
from django.contrib import admin
from test_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home,name="home")
]
