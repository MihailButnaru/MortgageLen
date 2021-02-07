from decimal import Decimal
from unittest import TestCase
from mortgage.views.calculator_view import CalculatorViewSet
from rest_framework import status
from django.test import RequestFactory

from mortgage.views.tests.mock_data import input_calculator_data


class TestCalculatorViewSet(TestCase):
    def setUp(self) -> None:
        self.input_data = input_calculator_data()
        self.factory = RequestFactory()

    def test_calculate_endpoint(self):
        request = self.factory.post(
            path="api/mortgage/calculator/",
            data=self.input_data,
            content_type="application/json",
        )

        response = CalculatorViewSet.as_view(actions={"post": "calculate"})(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            set(response.data),
            {
                "monthly_mortgage_payment",
                "total_interest_rate_amount",
                "total_mortgage_amount_with_interest_rate",
                "amortization_schedule",
            },
        )

        self.assertEqual(response.data["monthly_mortgage_payment"], Decimal("1448.41"))
        self.assertEqual(
            response.data["total_interest_rate_amount"], Decimal("23809.35")
        )
        self.assertEqual(
            response.data["total_mortgage_amount_with_interest_rate"],
            Decimal("173809.35"),
        )
