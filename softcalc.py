def payback():
    init_invest = int(input("initial investment: "))
    net_flow = int(input("net cash flow: "))

    result = init_invest/net_flow

    print(result)
    return True

def netcash():
    inflow = int(input("cash inflows: "))
    outflow = int(input("cash outflows: "))

    result = inflow - outflow

    print(result)
    return True

def breakeven():
    init_invest = int(input("initial investment: "))
    net_profit = int(input("net profit margin: "))

    result = init_invest / net_profit

    print(result)
    return True

def roi():
    benefits = int(input("total expected benefits: "))
    costs = int(input("total expected costs: "))

    result = ( (benefits - costs) / costs ) * 100
    print(result)

    return True

def netincome():
    benefits = int(input("total expected benefits: "))
    costs = int(input("total expected costs: "))

    result = benefits - costs
    
    print(result)
    return True

def discount():
    net_cash = int(input("Net cash flow: "))
    rate = float(input("discount rate: "))
    time_period = int(input("time period: "))

    result = float(net_cash / (1 + rate)**time_period)
    print(result)

    return True

def expduration():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    result = (a + (4*b) + c) / 6
    print(result)

    return True

def switch(choice):
    if(choice == 1):
        return payback()
    if(choice == 2):
        return netcash()
    if(choice == 3):
        return breakeven()
    if(choice == 4):
        return roi()
    if(choice == 5):
        return netincome()
    if(choice == 6):
        return discount()
    if(choice == 7):
        return expduration()
    if(choice == 9):
        return False

def main():
    quit = True

    while(quit):
        print("""
        Choose a calculation:
        1 - Payback Period
        2 - Net Cash Flow
        3 - Breakeven Point
        4 - Return on Investment
        5 - Net Income
        6 - Discounted Cash Flow
        7 - PERT Expected Duration
        9 - Quit""")

        choice = int(input())
        quit = switch(choice)

if __name__ == "__main__":
    main()
