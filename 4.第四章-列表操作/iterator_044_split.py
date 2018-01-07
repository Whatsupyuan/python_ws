
players = ['charles', 'martina', 'michael', 'florence', 'eli']
split_arr = players[0:1]
print(split_arr)

split_arr = players[1:]
print(split_arr)

# 内容指向一直的 list , 则两个list不能相互独立
new_players = players
new_players.insert(0,"yuan")
print(new_players)
print(players) ;

print()

# 复制列表 [:] , 复制之后的列表是独立的内存指向
new_players = players[:]
new_players.append("Kobe")
print(players)
print(new_players)