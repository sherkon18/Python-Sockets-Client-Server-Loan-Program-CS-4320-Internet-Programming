__author__ = 'Edward Mwangi'


'''
:formula --> Monthly = initial_balance * (1+rate)^n * rate / [(1+rate)^n -1]
:where rate = percentage / 1200
:argument: annualRate --> Percentage
:argument: initialBalance --> principal
'''

def compute_monthly_payment(initial_balance, annual_rate, number_of_months):
    rate = annual_rate / 1200

    return initial_balance * (1+rate)**number_of_months * rate / ((1+rate)**number_of_months - 1)


def interest_accrued(month, initial_balance, annual_rate, monthly_payment):
    if month < 1:
        print("month has to be 1 or greater")
        quit()
    else:
        rate = annual_rate / 1200
        return remaining_balance(month, initial_balance, annual_rate, monthly_payment) * rate


def remaining_balance(month, initial_balance, annual_rate, monthly_payment):
    if month < 1:
        print("month has to be 1 or greater")
        quit()
    elif month == 1:
        return initial_balance
    else:
        rem = remaining_balance(month - 1, initial_balance, annual_rate, monthly_payment)
        interest = interest_accrued(month - 1, initial_balance, annual_rate, monthly_payment)

        return rem + interest - monthly_payment


if __name__ == "__main__": # test code only
    st = "{:12s} {:18s} {:15s} {:15s} {:15s}".format('Month', 'Balance In', 'Interest', 'Payment', 'Balance Out')
    print(st)
    monthly_pay = compute_monthly_payment(10000, 10, 20)
    print("monthly payment: {:5.2f}".format(monthly_pay))

    print("\n\n")

    for month in range(1, 21):
        print("month {:2d} remaining bal = {:5.2f}".format(month, remaining_balance(month, 10000, 10, monthly_pay)))

    print("\n\n")

    for month in range(1, 21):
        print("month {:2d} interest accrued = {:5.2f}".format(month, interest_accrued(month, 10000, 10, monthly_pay)))
