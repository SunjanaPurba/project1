from django.contrib import admin
from django.urls import path
from app_F.views import book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_list),
]
