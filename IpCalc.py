import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', choices=['annuity', 'diff'])
parser.add_argument('-p1', '--principal')
parser.add_argument('-p2', '--periods')
parser.add_argument('-p3', '--payment')
parser.add_argument('-i', '--interest', default = '-100')

args = parser.parse_args()
variables = [args.type, args.principal, args.periods, args.payment, args.interest]

if args.type != 'annuity' and args.type != 'diff':
    print('Incorrect parameters')

elif args.type == 'diff' and args.payment:
    print('Incorrect parameters')

elif args.interest == '-100':
    print('Incorrect parameters')

elif len(variables) < 4:
    print('Incorrect parameters')

elif '-' in variables:
    print('Incorrect parameters')

if args.type == 'diff' and args.principal and args.periods and args.interest:
    principal = float(args.principal)
    periods = int(args.periods)
    interest = float(args.interest) / 100
    i = interest / 12
    payment = 0
    month = 1
    for period in range(1, periods + 1):
        step_one = principal * (month - 1)
        step_two = principal - step_one / periods
        step_three = i * step_two
        step_four = principal / periods + step_three
        step_four = math.ceil(step_four)
        print(f'Month {month}: payment is {step_four}')
        payment += step_four
        month += 1
    overpayment = payment - principal
    overpayment = int(overpayment)
    print()
    print(f'Overpayment = {overpayment}')

if args.type == 'annuity' and args.principal and args.periods and args.interest:
    principal = float(args.principal)
    periods = int(args.periods)
    interest = float(args.interest) / 100
    i = interest / 12
    first_step = i * math.pow(i + 1, periods)
    second_step = math.pow(1 + i, periods) - 1
    a = principal * first_step / second_step
    a = math.ceil(a)
    print(f'Your annuity payment = {a}!')
    payment = a * periods
    overpayment = payment - principal
    overpayment = int(overpayment)
    print(f'Overpayment = {overpayment}')

if args.type == 'annuity' and args.payment and args.periods and args.interest:
    periods = int(args.periods)
    interest = float(args.interest) / 100
    loan_payment = float(args.payment)
    i = interest / 12
    first_step = i * math.pow(1 + i, periods)
    second_step = math.pow(1 + i, periods) - 1
    third_step = first_step / second_step
    P = loan_payment / third_step
    P = math.floor(P)
    print(f'Your loan principal = {P}!')
    payment = loan_payment * periods
    overpayment = payment - P
    overpayment = int(overpayment)
    print(f'Overpayment = {overpayment}')

if args.type == 'annuity' and args.principal and args.payment and args.interest:
    principal = float(args.principal)
    interest = float(args.interest) / 100
    loan_payment = float(args.payment)
    i = interest / 12
    n = math.log(loan_payment / (loan_payment - i * principal), 1 + i)
    n = math.ceil(n)
    n = int(n)
    years = n / 12
    if years.is_integer():
        if years == 1:
            print('It will take 1 year to repay this loan!')
        else:
            years = int(years)
            print(f'It will take {years} years to repay this loan!')
    else:
        if n == 1:
            print('It will take 1 month to repay this loan!')
        elif years < 1:
            print(f'It will take {n} months to repay this loan!')
        else:
            years_print = math.floor(years)
            years_print = int(years_print)
            month_print = n - years_print * 12
            month_print = int(month_print)
            if month_print == 1:
                print(f'It will take {years_print} years and 1 month to repay this loan!')
            else:
                print(f'It will take {years_print} years and {month_print} months to repay this loan!')
    payment = loan_payment * n
    overpayment = payment - principal
    overpayment = int(overpayment)
    print(f'Overpayment = {overpayment}')
