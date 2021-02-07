"""
Amortization is the process of paying off a debt with a known repayment term in
regular installments over time.

This module is dealing with the calculations (amortization schedule, that shows
regularly scheduled payments and how they chip away at the loan balance over time).

"""
from datetime import date
from dateutil.relativedelta import relativedelta
from pydantic import BaseModel


class AmortizationSchedule(BaseModel):
    monthly: list
    annual: list
    monthly_mortgage_payment: float
    total_interest_rate_amount: float


class AmortizationCalculator:

    @staticmethod
    def payment_calc(
            mortgage_amount: float,
            years: int,
            interest: float
    ) -> float:
        number_months = years * 12

        interest_monthly = interest / 100 / 12

        numerator = interest_monthly * ((1 + interest_monthly) ** number_months)
        denominator = (1 + interest_monthly) ** number_months - 1

        payment = round(mortgage_amount * (numerator / denominator), 2)

        return payment

    @staticmethod
    def _construct_scheduled_payments(
            *,
            beginning_balance: float,
            interest_amount: float,
            principal_amount: float,
            ending_balance: float
    ) -> dict:
        return {
            "beginning_balance": beginning_balance,
            "interest_amount": interest_amount,
            "principal_amount": principal_amount,
            "remaining_balance": ending_balance
        }

    @classmethod
    def _construct_monthly_payments(
            cls,
            month: int,
            beginning_balance: float,
            interest_rate: float,
            mortgage_amount: float,
            ending_balance: float,
    ) -> dict:

        scheduled_payments = cls._construct_scheduled_payments(
            beginning_balance=beginning_balance,
            interest_amount=interest_rate,
            principal_amount=mortgage_amount,
            ending_balance=ending_balance
        )

        scheduled_payments["month"] = month

        return scheduled_payments

    @classmethod
    def _construct_annual_payments(
            cls,
            year,
            beginning_balance: float,
            interest: float,
            mortgage_amount: float,
            ending_balance: float
    ) -> dict:
        scheduled_payments = cls._construct_scheduled_payments(
            beginning_balance=beginning_balance,
            interest_amount=interest,
            principal_amount=mortgage_amount,
            ending_balance=ending_balance
        )

        scheduled_payments["year"] = year

        return scheduled_payments

    @classmethod
    def amortization_schedule(
            cls,
            mortgage_term: int,
            mortgage_amount: float,
            interest_rate: float
    ) -> AmortizationSchedule:
        """
            Calculate mortgage amortization (monthly, yearly)
                Args:
                    mortgage_term (int): term of the mortgage
                    interest_rate (float): interest rate of the mortgage
                    mortgage_amount (float); amount borrowed
                Returns:
                    Amortization schedule (annual, monthly)
        """
        monthly_data = []
        annual_data = []

        payment = cls.payment_calc(
            years=mortgage_term,
            interest=interest_rate,
            mortgage_amount=mortgage_amount
        )

        # total number of payments
        total_nr_payments = mortgage_term * 12

        # used to calculate the yearly (payments)
        year = 1

        monthly_rate = interest_rate / 100 / 12

        payment_monthly_date = date.today()  # starts from today
        payment_yearly_date = date.today()  # starts from today

        beginning_balance_per_month = mortgage_amount
        beginning_balance_per_year = mortgage_amount

        # interest rates
        interest_rate_per_year = 0
        principal_amount_per_year = 0

        # interest rate amount per year
        total_interest_rate_amount = 0

        for _ in range(total_nr_payments):
            interest = round(beginning_balance_per_month * monthly_rate, 2)
            principal_amount_per_month = round(payment - interest, 2)
            remaining_balance_per_month = round(beginning_balance_per_month - principal_amount_per_month, 2)

            interest_rate_per_year = interest_rate_per_year + interest
            principal_amount_per_year = principal_amount_per_year + principal_amount_per_month

            if year == 12:
                remaining_balance_per_year = beginning_balance_per_year - principal_amount_per_year

                annual_payment_payload = cls._construct_annual_payments(
                    year=payment_yearly_date,
                    interest=interest_rate_per_year,
                    mortgage_amount=principal_amount_per_year,
                    beginning_balance=beginning_balance_per_year,
                    ending_balance=remaining_balance_per_year
                )

                annual_data.append(annual_payment_payload)

                beginning_balance_per_year = remaining_balance_per_year
                payment_yearly_date = payment_yearly_date + relativedelta(years=+1)

                # interest rate amount per year
                total_interest_rate_amount = total_interest_rate_amount + interest_rate_per_year

                # reset the data
                interest_rate_per_year = 0
                principal_amount_per_year = 0
                year = 0

            monthly_payments = cls._construct_monthly_payments(
                month=payment_monthly_date,
                beginning_balance=beginning_balance_per_month,
                interest_rate=interest_rate,
                mortgage_amount=principal_amount_per_month,
                ending_balance=remaining_balance_per_month
            )

            monthly_data.append(monthly_payments)

            beginning_balance_per_month = remaining_balance_per_month
            payment_monthly_date = payment_monthly_date + relativedelta(months=+1)

            year += 1

        amortization_schedule = {
            "monthly": monthly_data,
            "annual": annual_data,
            "monthly_mortgage_payment": payment,
            "total_interest_rate_amount": total_interest_rate_amount
        }

        return AmortizationSchedule(**amortization_schedule)
