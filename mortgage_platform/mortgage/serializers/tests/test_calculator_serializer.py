from unittest import TestCase
from mortgage.serializers.calculator_serializer import (
    InputCalculatorSerializer,
    OutputCalculatorSerializer,
)


class TestInputCalculatorSerializer(TestCase):
    def setUp(self) -> None:
        self.input_data = {
            "property_value": 100000,
            "deposit_amount": 5000,
            "mortgage_term": 10,
            "interest_rate": 3.1,
        }

    def test_it_can_serialize_input_data(self):
        inst = InputCalculatorSerializer(data=self.input_data)
        assert inst.is_valid()

        self.assertEqual(set(inst.validated_data), set(self.input_data))


class TestOutputCalculatorSerializer(TestCase):
    def setUp(self) -> None:
        self.initial_data = {
            "monthly_mortgage_payment": 100,
            "total_interest_rate_amount": 100000,
            "total_mortgage_amount_with_interest_rate": 110000,
            "amortization_schedule": {
                "annual": [
                    {
                        "year": "2021-02-07",
                        "beginning_balance": 150000.0,
                        "interest_amount": 4321.42,
                        "principal_amount": 13059.5,
                        "remaining_balance": 136940.5,
                    },
                    {
                        "year": "2022-02-07",
                        "beginning_balance": 150000.0,
                        "interest_amount": 3000.42,
                        "principal_amount": 13059.5,
                        "remaining_balance": 136940.5,
                    },
                ],
                "monthly": [
                    {
                        "month": "2021-02-07",
                        "beginning_balance": 150000.0,
                        "interest_amount": 4321.42,
                        "principal_amount": 13059.5,
                        "remaining_balance": 136940.5,
                    },
                    {
                        "month": "2021-03-07",
                        "beginning_balance": 150000.0,
                        "interest_amount": 4321.42,
                        "principal_amount": 13059.5,
                        "remaining_balance": 122940.5,
                    },
                ],
            },
        }

    def test_it_can_serialize_output_data(self):

        inst = OutputCalculatorSerializer(data=self.initial_data)
        assert inst.is_valid()

        self.assertSetEqual(set(inst.validated_data), set(self.initial_data))
