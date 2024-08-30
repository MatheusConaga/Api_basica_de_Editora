from .api import api
from . import views
from django.urls import path

urlpatterns = [
    path('api/', api.urls),
    path('home/', views.home, name='home'),
]
