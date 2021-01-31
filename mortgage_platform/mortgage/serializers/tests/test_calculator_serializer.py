from unittest import TestCase
from mortgage.serializers.enums import RepaymentTypeEnum
from mortgage.serializers.calculator_serializer import (
    InputCalculatorSerializer,
    OutputCalculatorSerializer
)


class TestInputCalculatorSerializer(TestCase):
    def setUp(self) -> None:
        self.input_data = {
            "property_value": 100000,
            "repayment_type": RepaymentTypeEnum.REPAYMENT.name,
            "deposit_amount": 5000,
            "mortgage_term": 10,
            "interest_rate": 3.1
        }

    def test_it_can_serialize_input_data(self):
        inst = InputCalculatorSerializer(data=self.input_data)
        assert inst.is_valid()

        self.assertEqual(
            inst.validated_data,
            self.input_data
        )

    def test_it_can_serialize_repayment_type_interest(self):
        input_data = self.input_data
        input_data["repayment_type"] = RepaymentTypeEnum.INTEREST_ONLY.name

        inst = InputCalculatorSerializer(data=input_data)
        assert inst.is_valid()

        self.assertEqual(inst.validated_data, input_data)
        self.assertEqual(
            input_data["repayment_type"],
            RepaymentTypeEnum.INTEREST_ONLY.name
        )


class TestOutputCalculatorSerializer(TestCase):
    def setUp(self) -> None:
        self.initial_data = {
            "monthly_mortgage_payment": 100,
            "total_mortgage_amount": 100000,
            "total_mortgage_amount_interest_rate": 110000,
            "amortization_schedule": {
                "annual": [
                    {
                        "year": 1,
                        "beginning_balance": 10000.1,
                        "interest": 1.1,
                        "principal": 150000,
                        "ending_balance": 10000
                    },
                    {
                        "year": 2,
                        "beginning_balance": 10000.1,
                        "interest": 1.1,
                        "principal": 150000,
                        "ending_balance": 10000
                    }
                ],
                "monthly": [
                    {
                        "year": 1,
                        "table": [
                            {
                                "month": 1,
                                "beginning_balance": 10000.1,
                                "interest": 1.1,
                                "principal": 150000,
                                "ending_balance": 10000
                            },
                            {
                                "month": 2,
                                "beginning_balance": 50000.1,
                                "interest": 2.1,
                                "principal": 150000,
                                "ending_balance": 10000
                            }
                        ]
                    },
                    {
                        "year": 2,
                        "table": [
                            {
                                "month": 1,
                                "beginning_balance": 332323.1,
                                "interest": 1.1,
                                "principal": 150000,
                                "ending_balance": 23122
                            }
                        ]
                    }
                ]
            }
        }

    def test_it_can_serialize_output_data(self):

        inst = OutputCalculatorSerializer(data=self.initial_data)
        assert inst.is_valid()

        self.assertSetEqual(set(inst.validated_data), set(self.initial_data))
