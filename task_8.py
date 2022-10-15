money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


def acount(money_capital,salary,spend,increase):
    month = 0
    while True:
        money_capital -= spend
        spend *= (1 + increase)
        if money_capital > 0:
            month += 1
            money_capital += salary
        else :
            return month

print(acount(money_capital,salary,spend,increase))
