class CalculatorProcess:

    @staticmethod
    def _construct_data_for_calculations(input_data) -> dict:
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
    def mortgage_calculator(
            mortgage_amount: int,
            years: int,
            interest: float
    ) -> float:
        interest = interest / 100
        number_months = years * 12

        interest_monthly = interest / 12

        numerator = interest_monthly * ((1 + interest_monthly) ** number_months)
        denominator = (1 + interest_monthly) ** number_months - 1

        payment = mortgage_amount * (numerator / denominator)

        return payment

    @classmethod
    def calculate(cls, input_data: dict) -> float:
        data_for_calculations = cls._construct_data_for_calculations(
            input_data=input_data
        )

        mortgage_amount = cls.mortgage_calculator(
            interest=data_for_calculations["interest_rate"],
            years=data_for_calculations["mortgage_term"],
            mortgage_amount=data_for_calculations["mortgage_amount"]
        )

        return mortgage_amount

    @staticmethod
    def _construct_monthly_data(mortgage: dict):
        pass

    @staticmethod
    def _construct_annual_data(mortgage: dict):
        pass

    @classmethod
    def _construct_output_data(cls, mortgage: dict) -> dict:

        amortization_schedule = {
            "monthly": cls._construct_annual_data(mortgage=mortgage),
            "annual": cls._construct_annual_data(mortgage=mortgage)
        }

        return {
            "total_mortgage_amount": "",
            "monthly_mortgage_payment": "",
            "total_mortgage_amount_interest_rate": 0,
            "amortization_schedule": amortization_schedule
        }
