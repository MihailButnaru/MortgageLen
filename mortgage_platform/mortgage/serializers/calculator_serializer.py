from rest_framework import serializers
from mortgage.serializers.enums import RepaymentTypeEnum


class InputCalculatorSerializer(serializers.Serializer):
    property_value = serializers.DecimalField(
        min_value=0, max_digits=12, decimal_places=2, required=True
    )
    repayment_type = serializers.ChoiceField(
        choices=RepaymentTypeEnum.choices(), required=True
    )
    deposit_amount = serializers.DecimalField(
        min_value=0, max_digits=12, decimal_places=2, required=True
    )
    mortgage_term = serializers.IntegerField(
        min_value=10, max_value=40, required=True
    )
    interest_rate = serializers.FloatField(
        min_value=0, required=True
    )
