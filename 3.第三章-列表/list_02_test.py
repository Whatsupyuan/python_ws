#3.4
guestArr=["Kobe","James","Irving"] ;
print(guestArr) ;

#3.5
newGuest = "Jordan";
lostGuest = guestArr.pop(-1);
print("未能参加的嘉宾:" + lostGuest) ;
guestArr.append(newGuest);
print(guestArr) ;

#3.6
print("I have a bigger table") ;
guestArr.insert(0,"yuan");
guestArr.insert(2,"Jack");
guestArr.append("Eminem");
print(guestArr) ;

#3.7
print("Remove tow guest");
lost_g1 = guestArr.pop(-1);
print("So sorry :" + lost_g1) ;
lost_g1 = guestArr.pop(-1);
print("So sorry :" + lost_g1) ;
lost_g1 = guestArr.pop(-1);
print("So sorry :" + lost_g1) ;
lost_g1 = guestArr.pop(-1);
print("So sorry :" + lost_g1) ;
print(guestArr);
del guestArr[-1];
del guestArr[-1];
print("最后的邀请名单:") ;
print(guestArr) ;
