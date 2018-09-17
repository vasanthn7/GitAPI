from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.user_view)

urlpatterns = [
    path('', include(router.urls)),
    path(r'search/',views.home, name='home'),
]
