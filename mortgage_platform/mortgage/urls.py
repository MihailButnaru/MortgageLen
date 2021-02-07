from django.urls import path

from mortgage.views import CalculatorViewSet

urlpatterns = [
    path(
        "calculator/",
        CalculatorViewSet.as_view(actions={"post": "calculate"}),
        name="calculator-detail",
    )
]
