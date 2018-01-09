# 7-8
andwich_orders = ["sandwish01", "sandwish02", "sandwish03"]
finished_sandwiches = []
while andwich_orders:
    ao = andwich_orders.pop()
    print("I made your tuna " + ao)
    finished_sandwiches.append(ao)
print(finished_sandwiches)

print()

# 7-9 去除 list 中所有的pastrami
andwich_orders = ["sandwish01", "sandwish02", "sandwish03", "pastrami", "pastrami", "pastrami"]
print(andwich_orders)
finished_sandwiches = []
while "pastrami" in andwich_orders:
    andwich_orders.remove("pastrami")
print(andwich_orders)


# 7-10 调查结果
result = {}
flag = True
while flag:
    name = input("What's your name?")
    place = input("If you could visit one place in the world, where would you go?")
    result[name] = place
    que = input("Would you let anthor one do this ?(Yes/No)")
    if que.lower() == "no":
        flag = False
for name , place in result.items():
    print(name + " want go to " + place)



