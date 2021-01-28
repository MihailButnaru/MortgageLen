from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from mortgage.serializers.calculator_serializer import InputCalculatorSerializer


class CalculatorViewSet(ViewSet):

    def calculate(self, request):

        input_serializer = InputCalculatorSerializer(data=request.data)

        if not input_serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=input_serializer.errors)

        return Response(status=status.HTTP_201_CREATED, data=input_serializer.validated_data)
