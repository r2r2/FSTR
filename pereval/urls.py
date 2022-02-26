from django.urls import path, include
from rest_framework import routers

from pereval import views


router = routers.DefaultRouter()
router.register(r'submitData', views.SubmitDataViewSet, basename='submitData')


urlpatterns = [
    path('', include(router.urls)),
]
