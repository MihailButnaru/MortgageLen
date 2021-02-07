from decimal import Decimal
from unittest import TestCase
from mortgage.processes.calculator_process import CalculatorProcess
from mortgage.views.tests.mock_data import input_calculator_data


class TestCalculatorProcess(TestCase):
    def setUp(self) -> None:
        self.calculator_process = CalculatorProcess
        self.input_data = input_calculator_data()

        self.expected_output_data = {
            "monthly_mortgage_payment",
            "total_mortgage_amount_with_interest_rate",
            "total_interest_rate_amount",
            "amortization_schedule",
        }

    def test__construct_data_for_calculations(self):

        data_for_calculations = (
            self.calculator_process._construct_data_for_calculations(
                input_data=self.input_data
            )
        )

        expected_data = {
            "mortgage_amount": self.input_data["property_value"],
            "interest_rate": self.input_data["interest_rate"],
            "mortgage_term": self.input_data["mortgage_term"],
        }

        self.assertEqual(data_for_calculations, expected_data)

    def test__construct_data_for_calculations_with_deposit_amount(self):

        input_data = self.input_data
        input_data["deposit_amount"] = 100

        data_for_calculations = (
            self.calculator_process._construct_data_for_calculations(
                input_data=input_data
            )
        )

        expected_data = {
            "mortgage_amount": (
                input_data["property_value"] - input_data["deposit_amount"]
            ),
            "interest_rate": input_data["interest_rate"],
            "mortgage_term": input_data["mortgage_term"],
        }

        self.assertEqual(data_for_calculations, expected_data)

    def test__construct_output_data(self):

        output_data = self.calculator_process._construct_output_data(
            mortgage_amount=self.input_data["property_value"],
            monthly_payments=[],
            annual_payments=[],
            total_interest_rate_amount=self.input_data["interest_rate"],
            monthly_mortgage_payment=self.input_data["interest_rate"]
            + self.input_data["property_value"],
        )

        expected_output_data = {
            "total_mortgage_amount_with_interest_rate": (
                self.input_data["interest_rate"] + self.input_data["property_value"]
            ),
            "total_interest_rate_amount": self.input_data["interest_rate"],
            "monthly_mortgage_payment": (
                self.input_data["interest_rate"] + self.input_data["property_value"]
            ),
            "amortization_schedule": {"monthly": [], "annual": []},
        }

        self.assertEqual(output_data, expected_output_data)

    def test_process_mortgage_payments(self):

        mortgage_payments = self.calculator_process.process_mortgage_payments(
            mortgage_amount=self.input_data["property_value"],
            mortgage_term=self.input_data["mortgage_term"],
            interest_rate=self.input_data["interest_rate"],
        )

        self.assertEqual(set(mortgage_payments), self.expected_output_data)

        self.assertEqual(
            mortgage_payments["total_mortgage_amount_with_interest_rate"],
            round(Decimal(173809.35), 2),
        )

    def test_calculate(self):

        calculate_mortgage = self.calculator_process.calculate(
            input_data=self.input_data
        )

        self.assertEqual(set(calculate_mortgage), self.expected_output_data)
