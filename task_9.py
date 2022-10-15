
salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

def acount(month,salary,spend,increase):
    need_money = 0
    i = 0
    while i < month:
        need_money += spend
        spend *= (1 + increase)
        i += 1


    need_money -= salary * month
    need_money = round(need_money)
    return need_money

print(acount(months,salary,spend,increase))
