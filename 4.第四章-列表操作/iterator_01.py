cars = ["bmw", "benz", "audi", "toyota"]
cars_copy = []
for cat in cars:
    print(cat)
    print(cars)
    cars_copy.append(cat)
print(str(cars_copy).title())



# ----------------------------------------------------------------
# 分号的使用,在python语言中尽量不要使用 ; 号做为行结束
# ; 真实的用法
x=1;y=2;z=3;
print(x);
print(y);
print(z);