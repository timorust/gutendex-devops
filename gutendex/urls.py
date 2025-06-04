# gutendex/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html')),  
    path('api/', include(router.urls)),  
]
