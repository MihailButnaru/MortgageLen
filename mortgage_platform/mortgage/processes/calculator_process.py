from decimal import Decimal
from mortgage.processes.amortization_calculations import AmortizationCalculator


class CalculatorProcess:

    @staticmethod
    def _construct_data_for_calculations(input_data: dict) -> dict:
        deposit_amount = input_data["deposit_amount"]
        property_value = input_data["property_value"]

        if deposit_amount >= 0:
            property_value = property_value - deposit_amount

        return {
            "mortgage_amount": property_value,
            "interest_rate": input_data["interest_rate"],
            "mortgage_term": input_data["mortgage_term"]
        }

    @staticmethod
    def _construct_output_data(
            *,
            mortgage_amount: float,
            monthly_payments: list,
            annual_payments: list,
            total_interest_rate_amount: float,
            monthly_mortgage_payment: float
    ) -> dict:
        amortization_schedule = {
            "monthly": monthly_payments,
            "annual": annual_payments
        }

        total_mortgage_amount = round(Decimal(total_interest_rate_amount), 2) + mortgage_amount

        return {
            "total_interest_rate_amount": total_interest_rate_amount,
            "total_mortgage_amount_with_interest_rate": total_mortgage_amount,
            "monthly_mortgage_payment": monthly_mortgage_payment,
            "amortization_schedule": amortization_schedule
        }

    @classmethod
    def process_mortgage_payments(
            cls,
            mortgage_amount: float,
            mortgage_term: int,
            interest_rate: float
    ):
        amortization_schedule = AmortizationCalculator.amortization_schedule(
            mortgage_amount=mortgage_amount,
            mortgage_term=mortgage_term,
            interest_rate=interest_rate
        )

        return cls._construct_output_data(
            mortgage_amount=mortgage_amount,
            annual_payments=amortization_schedule.annual,
            monthly_payments=amortization_schedule.monthly,
            total_interest_rate_amount=amortization_schedule.total_interest_rate_amount,
            monthly_mortgage_payment=amortization_schedule.monthly_mortgage_payment
        )

    @classmethod
    def calculate(cls, input_data: dict) -> dict:
        data_for_calculations = cls._construct_data_for_calculations(
            input_data=input_data
        )

        return cls.process_mortgage_payments(
            interest_rate=data_for_calculations["interest_rate"],
            mortgage_term=data_for_calculations["mortgage_term"],
            mortgage_amount=data_for_calculations["mortgage_amount"]
        )
