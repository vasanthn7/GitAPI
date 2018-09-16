from django.urls import path,include
from rest_framework import routers
from users.views import user_view

router = routers.DefaultRouter()
router.register('users', user_view)

urlpatterns = [
    path('', include(router.urls))
]
