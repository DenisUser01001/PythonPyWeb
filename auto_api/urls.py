from django.urls import path

from auto_api import views

urlpatterns = [
    path("autos/", views.ListCreateAutoAPIView.as_view(), name="auto-list"),
    path("autos/<int:pk>/", views.RetrieveUpdateDeleteAutoAPIView.as_view(), name="auto-detail"),
]
