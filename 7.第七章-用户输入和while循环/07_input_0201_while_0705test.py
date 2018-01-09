# 电影院
while True:
    info = int(input("岁数?"))
    if info == 888:
        break
    if info < 3:
        print("免费")
    elif info > 3 and info < 12:
        print("10美元")
    elif info > 15:
        print("15美元")
