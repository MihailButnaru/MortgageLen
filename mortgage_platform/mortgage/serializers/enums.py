from enum import Enum


class RepaymentTypeEnum(Enum):
    REPAYMENT = "REPAYMENT"
    INTEREST = "INTEREST"

    @classmethod
    def choices(cls):
        return tuple(
            (repayment_type.name, repayment_type.value) for repayment_type in cls
        )
