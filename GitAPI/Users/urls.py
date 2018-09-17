from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.user_view)

urlpatterns = [
    path('',views.home, name='home')
    # path(r'^users/', include(router.urls))
]
