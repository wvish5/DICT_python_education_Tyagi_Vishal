import math
import sys

print("Loan principal: 1000")
print("Month 1: repaid 250")
print("Month 2: repaid 250")
print("Month 3: repaid 500")
print("The loan has been repaid!")
a = int(input("Enter the loan principal:"))
b = input('What do you want to calculate?\ntype "m" for number of monthly payments,\ntype "p" for the monthly payment:')
if b == "m":
    c = int(input("Enter the monthly payment:"))
    q = a/c
    q = math.ceil(q)
    if q == 1:
        print(f"It will take {q} month to repay the loan")
    else:
        print(f"It will take {q} months to repay the loan")
elif b == "p":
    c = int(input("Enter the monthly payment:"))
    z = a/c
    z = math.ceil(z)
    w = a-(c-1)*z
    print("")
    print(f"Your monthly payment = {z} and the last payment = {w}.")
print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
calc = input()
if calc == 'n':
    print('Enter the loan principal:')
    loan_principal = int(input())
    print('Enter the monthly payment:')
    m_payment = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / 1200
    n = math.ceil(math.log(m_payment / (m_payment - i * loan_principal), 1 + i))
    n_years = math.floor(n / 12)
    n_months = n % 12
    if n_years > 1 and n_months > 1:
        print(f'It will take {n_years} years and {n_months} months to repay this loan!')
    elif n_years == 1 and n_months > 1:
        print(f'It will take {n_years} year and {n_months} months to repay this loan!')
    elif n_years == 1 and n_months == 1:
        print(f'It will take {n_years} year and {n_months} month to repay this loan!')
    elif n_years == 0 and n_months == 1:
        print(f'It will take {n_months} month to repay this loan!')
    elif n_years == 0 and n_months > 1:
        print(f'It will take {n_months} months to repay this loan!')
    elif n_years > 1 and n_months == 0:
        print(f'It will take {n_years} years to repay this loan!')
    elif n_years == 1 and n_months == 0:
        print(f'It will take {n_years} year to repay this loan!')
elif calc == 'a':
    print('Enter the loan principal:')
    loan_principal = int(input())
    print('Enter the number of periods:')
    n_periods = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / 1200
    a = math.ceil(loan_principal * ((i * math.pow((1 + i), n_periods)) / (math.pow((1 + i), n_periods) - 1)))
    print(f'Your monthly payment = {a}!')
elif calc == 'p':
    print('Enter the annuity payment:')
    a_payment = float(input())
    print('Enter the number of periods:')
    n_periods = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / 1200
    p = round(a_payment / ((i * math.pow((1 + i), n_periods)) / (math.pow((1 + i), n_periods) - 1)))
    print(f'Your loan principal = {p}!')
args = sys.argv

type_ = False
principal = False
periods = False
interest = False
payment = False

for i in range(len(args)):
    if args[i].split("=")[0] == "--type":
        type_ = args[i].split("=")[1]
    elif args[i].split("=")[0] == "--principal":
        principal = int(args[i].split("=")[1])
    elif args[i].split("=")[0] == "--periods":
        periods = int(args[i].split("=")[1])
    elif args[i].split("=")[0] == "--interest":
        interest = float(args[i].split("=")[1])
    elif args[i].split("=")[0] == "--payment":
        payment = int(args[i].split("=")[1])

if type_ == "diff":
    if principal and periods and interest:
        i = interest / (12 * 100)
        total = 0
        for m in range(1, periods + 1):
            d = math.ceil(principal / periods + i * (principal - (principal * (m - 1)) / periods))
            print(f"Month {m}: payment is {d}")
            total += d
        print()
        print(f"Overpayment = {total - principal}")
    else:
        print("Incorrect parameters.")
elif type_ == "annuity":
    if principal and periods and interest:
        i = interest / (12 * 100)
        annuity = math.ceil(principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
        print(f"Your annuity payment = {annuity}!")
        print(f"Overpayment = {annuity * periods - principal}")
    elif payment and periods and interest:
        i = interest / (12 * 100)
        principal = math.floor(payment / (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1)))
        print(f"Your loan principal = {principal}!")
        print(f"Overpayment = {payment * periods - principal}")
    elif principal and payment and interest:
        i = interest / (12 * 100)
        periods = math.log(payment / (payment - i * principal), 1 + i)
        periods = math.ceil(periods)
        and_ = ""
        n_years = str(periods // 12) + " years"
        n_months = str(periods % 12) + " months"
        if periods // 12 != 0 and periods % 12 != 0:
            and_ = " and "
        elif periods // 12 == 0:
            n_years = ""
        elif periods % 12 == 0:
            n_months = ""
        print(f"It will take {n_years}{and_}{n_months} to repay this loan!")
        print(f"Overpayment = {periods * payment - principal}")
    else:
        print("Incorrect parameters.")
else:
    print("Incorrect parameters.")

