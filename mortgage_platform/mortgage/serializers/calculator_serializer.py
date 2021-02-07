from rest_framework import serializers


def amount_field(min_value=0, max_digits=12, decimal_places=2, required=True):
    return serializers.DecimalField(
        min_value=min_value,
        max_digits=max_digits,
        decimal_places=decimal_places,
        required=required,
    )


class InputCalculatorSerializer(serializers.Serializer):
    property_value = amount_field()
    deposit_amount = amount_field()
    mortgage_term = serializers.IntegerField(min_value=10, max_value=40, required=True)
    interest_rate = amount_field()


class AnnualSerializer(serializers.Serializer):
    year = serializers.DateField()
    beginning_balance = amount_field()
    interest_amount = serializers.FloatField(min_value=0)
    principal_amount = amount_field()
    remaining_balance = amount_field()


class MonthlyDividerSerializer(serializers.Serializer):
    month = serializers.DateField()
    beginning_balance = amount_field()
    interest_amount = serializers.FloatField(min_value=0)
    principal_amount = amount_field()
    remaining_balance = amount_field()


class AmortizationScheduleSerializer(serializers.Serializer):
    annual = AnnualSerializer(many=True, allow_null=True)
    monthly = MonthlyDividerSerializer(many=True, allow_null=True)


class OutputCalculatorSerializer(serializers.Serializer):
    monthly_mortgage_payment = amount_field()
    total_interest_rate_amount = amount_field()
    total_mortgage_amount_with_interest_rate = amount_field()
    amortization_schedule = AmortizationScheduleSerializer(many=False, allow_null=True)
