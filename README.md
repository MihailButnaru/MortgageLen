# MortgageLen API
<hr/>

## Introduction

The MortgageLen API is a RestFul API that allows you to calculate the monthly or annual payments
based on the interest rate provided. The API gives you access to all the
mortgage loan functions (calculator) and allows you to find out the
(Monthly payment, interest rate, beginning balance, remaining balance and more..)


### What is a Mortgage
A Mortgage is a loan taken out to buy a property or land. Most run for 25 years,
but the term can be shorter or longer. The loan is secured against the
value of your home until it's paid off. If you can't keep up your
repayments the lender can repossess your home and sell it to get their
money back.

### What is amortization
Amortization is the process of spreading out a loan into a series of fixed payments. The loan
is paid off at the end of the payment schedule. Some of each payment goes towards interest costs,
and some goes toward your loan balance. Over time, you pass less in interest and more
toward your balance.

## API Specification

#### Endpoints Structure

| Endpoint | Method | Description |
| --------|:---------:|:----------|
| /api/mortgage/calculator/ | POST | Calculates the monthly/annual payment of the mortgage |

#### Endpoint Example
```
Request:
POST /api/mortgage/calculator/

    {
        "property_value": 150000,  # property value (the amount borrowed from a lender or bank)
        "deposit_amount": 0, # the upfront payment of the purchase
        "mortgage_term": 10, # the amount of time over which the loan must be repaid in full
        "interest_rate": 3.0, # the rate of interest charged by a mortgage lender
    }

    Response:
    {
        "monthly_mortgage_payment": 100,
        "total_interest_rate_amount": 100000,
        "total_mortgage_amount_with_interest_rate": 110000,
        "amortization_schedule": {
            "annual": [
                {
                    "year": "2021-02-07",
                    "beginning_balance": 150000.0,
                    "interest_amount": 4321.42,
                    "principal_amount": 13059.5,
                    "remaining_balance": 136940.5,
                },
                {
                    "year": "2022-02-07",
                    "beginning_balance": 150000.0,
                    "interest_amount": 3000.42,
                    "principal_amount": 13059.5,
                    "remaining_balance": 136940.5,
                },
            ],
            "monthly": [
                {
                    "month": "2021-02-07",
                    "beginning_balance": 150000.0,
                    "interest_amount": 4321.42,
                    "principal_amount": 13059.5,
                    "remaining_balance": 136940.5,
                },
                {
                    "month": "2021-03-07",
                    "beginning_balance": 150000.0,
                    "interest_amount": 4321.42,
                    "principal_amount": 13059.5,
                    "remaining_balance": 122940.5,
                },
            ],
        }
    }
    
```



#### HTTP RESPONSE CODES

| RESPONSE CODE | MESSAGE    |
| ------------- |:----------:|
| 200 OK        | All is well|
| 201 CREATED   | A resource has been created |
| 400 BAD REQUEST | Your request has missing arguments |
| 405 METHOD NOT ALLOWED | You are using an incorrect HTTP verb |
| 404 NOT FOUND | The endpoint requested does not exist |
| 500 INTERNAL SERVER ERROR | Something is wrong on our end |


## License & Author
License 2021 © MIHAIL BUTNARU

Made by Mihail Butnaru