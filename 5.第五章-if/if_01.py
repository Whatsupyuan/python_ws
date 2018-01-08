cars = ["benz","bmw","toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


print()

# 打印字符串判断结果
# 使用"=="进行判断
car = "bmw"
print(car == 'bmw')
print(car == 1)

# 操作之后对象指向赋值不变
print(car.upper() == "Bwm")
print(car)