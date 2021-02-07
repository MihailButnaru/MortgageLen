from unittest import TestCase

from datetime import date
from mortgage.processes.amortization_calculations import AmortizationCalculator
from mortgage.views.tests.mock_data import input_calculator_data


class TestAmortizationCalculator(TestCase):
    def setUp(self) -> None:
        self.input_data = input_calculator_data()
        self.amortization = AmortizationCalculator

        self.payments = {
            "beginning_balance": 102321,
            "interest_amount": 1232.3,
            "principal_amount": 145233,
            "remaining_balance": 100000,
        }
        self.payment_date = date(2021, 10, 1)

    def test_payment_calc(self):

        payment = self.amortization.payment_calc(
            mortgage_amount=self.input_data["property_value"],
            years=self.input_data["mortgage_term"],
            interest=self.input_data["interest_rate"],
        )

        self.assertEqual(payment, 1448.41)

    def test__construct_scheduled_payments(self):

        scheduled_payload = self.amortization._construct_scheduled_payments(
            beginning_balance=self.payments["beginning_balance"],
            interest_amount=self.payments["interest_amount"],
            principal_amount=self.payments["principal_amount"],
            ending_balance=self.payments["remaining_balance"],
        )

        self.assertEqual(scheduled_payload, self.payments)

    def test__construct_monthly_payments(self):

        monthly_payments = self.amortization._construct_monthly_payments(
            month=self.payment_date,
            beginning_balance=self.payments["beginning_balance"],
            interest_amount=self.payments["interest_amount"],
            principal_amount=self.payments["principal_amount"],
            ending_balance=self.payments["remaining_balance"],
        )

        expected_monthly_payments = self.payments
        expected_monthly_payments["month"] = self.payment_date

        self.assertEqual(monthly_payments, expected_monthly_payments)

    def test__construct_annual_payments(self):

        annual_payments = self.amortization._construct_annual_payments(
            year=self.payment_date,
            beginning_balance=self.payments["beginning_balance"],
            interest_amount=self.payments["interest_amount"],
            principal_amount=self.payments["principal_amount"],
            ending_balance=self.payments["remaining_balance"],
        )

        expected_annual_payments = self.payments
        expected_annual_payments["year"] = self.payment_date

        self.assertEqual(annual_payments, expected_annual_payments)

    def test_amortization_schedule(self):

        amortization_schedule = self.amortization.amortization_schedule(
            mortgage_term=self.input_data["mortgage_term"],
            mortgage_amount=self.input_data["property_value"],
            interest_rate=self.input_data["interest_rate"],
        )

        self.assertEqual(
            round(amortization_schedule.total_interest_rate_amount, 2), 23809.35
        )

        self.assertEqual(
            round(amortization_schedule.monthly_mortgage_payment, 2), 1448.41
        )
