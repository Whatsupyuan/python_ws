flag = True
while flag:
    name = input("Pleas input your name ... ")
    if name and name == 'q':
        flag = False
        continue
    with open("guest.txt", "a") as file:
        file.write(name + "\n")