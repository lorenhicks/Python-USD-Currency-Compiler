def compile_all_currency(unit):
    total_change = int(input())
    if total_change > 0:
        total_change_dollars = total_change / 100
        if total_change_dollars < 1:
            print("", end='')
        elif (total_change_dollars < 2):
            d1currency = "Dollar"
            print(int(total_change_dollars), d1currency)
        elif (total_change_dollars > 1):
            d1currency = "Dollars"
            print(int(total_change_dollars), d1currency)
        total_change_quarters = (total_change % 100) / 25
        if total_change_quarters < 1:
            print("", end='')
        elif (total_change_quarters < 2):
            qcurrency = "Quarter"
            print(int(total_change_quarters), qcurrency)
        elif (total_change_quarters > 1):
            qcurrency = "Quarters"
            print(int(total_change_quarters), qcurrency)
        total_change_dimes = (total_change % 100 % 25) / 10
        if total_change_dimes < 1:
            print("", end='')
        elif (total_change_dimes < 2):
            dcurrency = "Dime"
            print(int(total_change_dimes), dcurrency)
        elif (total_change_dimes > 1):
            dcurrency = "Dimes"
            print(int(total_change_dimes), dcurrency)
        total_change_nickels = (total_change % 100 % 25 % 10) / 5
        if total_change_nickels < 1:
            print("", end='')
        elif (total_change_nickels < 2):
            ncurrency = "Nickel"
            print(int(total_change_nickels), ncurrency)
        elif (total_change_nickels > 1):
            ncurrency = "Nickels"
            print(int(total_change_nickels), ncurrency)
        total_change_pennies = (total_change % 100 % 25 % 10 % 5) / 1
        if total_change_pennies < 1:
            print("", end='')
        elif (total_change_pennies < 2):
            pcurrency = "Penny"
            print(int(total_change_pennies), pcurrency)
        elif (total_change_pennies > 1):
            pcurrency = "Pennies"
            print(int(total_change_pennies), pcurrency)
    else:
        print("No change")