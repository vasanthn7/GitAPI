from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.user_all)

urlpatterns = [
    path(r'search/',views.home, name='home'),
    # path(r'user/', views.user_filter.as_view(),name='filter'),
    path('', include(router.urls)),
    # path(r'^user/', views.user_name.as_view(), name='bydate'),
]
