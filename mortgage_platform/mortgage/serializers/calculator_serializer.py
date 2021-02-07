from rest_framework import serializers
from mortgage.serializers.enums import RepaymentTypeEnum


def amount_field(min_value=0, max_digits=12, decimal_places=2, required=True):
    return serializers.DecimalField(
        min_value=min_value,
        max_digits=max_digits,
        decimal_places=decimal_places,
        required=required,
    )


class InputCalculatorSerializer(serializers.Serializer):
    property_value = amount_field()
    repayment_type = serializers.ChoiceField(
        choices=RepaymentTypeEnum.choices(), required=True
    )
    deposit_amount = amount_field()
    mortgage_term = serializers.IntegerField(
        min_value=10, max_value=40, required=True
    )
    interest_rate = amount_field()


class AnnualSerializer(serializers.Serializer):
    year = serializers.DateField()
    beginning_balance = amount_field()
    interest_amount = serializers.FloatField(
        min_value=0
    )
    principal_amount = amount_field()
    remaining_balance = amount_field()


class MonthlyDividerSerializer(serializers.Serializer):
    month = serializers.DateField()
    beginning_balance = amount_field()
    interest_amount = serializers.FloatField(
        min_value=0
    )
    principal_amount = amount_field()
    remaining_balance = amount_field()


class MonthlySerializer(serializers.Serializer):
    year = serializers.IntegerField(min_value=1)
    table = MonthlyDividerSerializer(many=True)


class AmortizationScheduleSerializer(serializers.Serializer):
    annual = AnnualSerializer(many=True)
    monthly = MonthlyDividerSerializer(many=True)


class OutputCalculatorSerializer(serializers.Serializer):
    monthly_mortgage_payment = amount_field()
    total_interest_rate_amount = amount_field()
    total_mortgage_amount_with_interest_rate = amount_field()
    amortization_schedule = AmortizationScheduleSerializer(many=False)
