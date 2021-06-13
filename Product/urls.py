from django.urls import path, include
from .views import ProductView
from rest_framework import routers


router = routers.SimpleRouter()
router.register('home', ProductView)

urlpatterns = [
    path('', include(router.urls))
]
