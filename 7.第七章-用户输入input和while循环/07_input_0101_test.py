# 7-1
carRequest = input();
print("Let me see if i can find you a " + carRequest)

# 7-2
restaurantQuestion=input("How many people?")
restaurantQuestion = int(restaurantQuestion)
if restaurantQuestion > 8:
    print("无座位")
else:
    print("有空桌")

# 7-3
judgeNum = int(input())
if judgeNum % 10 > 0:
    print("非10的整数倍")
else:
    print("10的整数倍")
