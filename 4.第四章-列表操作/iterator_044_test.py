# 4-10
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The first three items in the list are" )
print(players[:3])

print()


# python3 四舍五入 问题
# 官方文档写了，round(number[, ndigits]) values are rounded to the closest multiple of 10 to the power minus ndigits;
# if two multiples are equally close, rounding is done toward the even choice
# (so, for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2).
# 就是说round(1/2)取离它最近的整数，如果2个数（0和1）离它一样近，则取偶数（the even choice）。
# 因此round(1.5)=2, round(2.5)=2, round(3.5)=4, round(4.5)=4。
# http://www.cnblogs.com/lxmwb/p/7988913.html
# 4-10-2 打印列表中间的3个元素
print("Three items from the middle of the list are:")
import decimal
half_length = len(players)
a = decimal.Decimal(half_length)/2
decimal.getcontext().rounding = decimal.ROUND_UP
half_num = round(a,0)
print(players[int(half_num-2):int(half_num+1)])

print()

# 4-10-3 打印列表尾部的3个元素
print("The last three items in the list are:")
print(players[half_length-3:])

# 4-11-1
pizzas = ["one_pizza" , "two_pizza" , "thress_pizza"]
friend_pizzas = pizzas[:]
pizzas.append("none-pizza");
print(pizzas)
print(friend_pizzas)


for p in pizzas:
    print(p)