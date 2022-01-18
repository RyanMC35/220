"""

Ryan Campbell
lab1.py
Problem Description - The purpose of the lab is to create a chain of code that can compute the monthly
interest of a credit card.
Certificate of Authenticity - I, Ryan Campbell, certify that this lab is entirely my own work.

"""


def monthly_interest_charge():
    annual_interest = eval(input("What is your annual interest rate?:"))
    days_in_cycle = eval(input("What are the number of days in your billing cycle?:"))
    previous_balance = eval(input("What is your previous balance?:"))
    payment_amount = eval(input("What is your payment amount?:"))
    day_of_payment = eval(input("What day of the billing cycle was your payment made?:"))
    step_1 = previous_balance * days_in_cycle
    step_2 = payment_amount * (days_in_cycle - day_of_payment)
    step_3 = step_1 - step_2
    avg_daily_balance = step_3 / days_in_cycle
    monthly_interest = round(avg_daily_balance * ((annual_interest / 100) / 12), 2)
    print("Monthly Interest Charge: $", monthly_interest)
