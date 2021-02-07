from django.urls import path, include

urlpatterns = [path("api/mortgage/", include("mortgage.urls"))]
