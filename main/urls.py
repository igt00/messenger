from django.urls import path

from main.views import MainAPIView

urlpatterns = [
    path('', MainAPIView.as_view(), name='main'),
]