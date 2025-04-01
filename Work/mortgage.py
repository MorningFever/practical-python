# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
payment_this_month = payment
total_paid = 0.0
total_months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    total_months = total_months + 1

    principal = principal * (1 + rate / 12)
    if extra_payment_start_month <= total_months <= extra_payment_end_month:
        payment_this_month = payment + extra_payment
    else:
        payment_this_month = payment

    if(principal > payment_this_month):
        principal = principal - payment_this_month
        total_paid = total_paid + payment_this_month
    else:
        total_paid = total_paid + principal
        principal = 0

    print(f'Current Months : {total_months} / Payed : {round(total_paid, 2)} / Remain: {round(principal,2)}')


print('Total Months', total_months)
print('Total paid', round(total_paid, 2))