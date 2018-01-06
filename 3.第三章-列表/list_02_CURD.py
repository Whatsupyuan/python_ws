'''
数组操作 CURD

添加 : append(value);
插入元素 : insert(targetIndex , value);

删除:
根据Index删除: del , pop
根据值删除 : remove(value);
'''
nameArr = ["Kobe","James","Yuan"];
nameArr.append("911");
print(nameArr);
print(nameArr[-1]) ; 

print();

# append 创建空列表进行数据存储
emptyArr = [];
emptyArr.append("Kobe");
emptyArr.append("yuan");
print(emptyArr[0]);
print(emptyArr[-1]);

# insert 插入数值
emptyArr.insert(1,"James") ;
emptyArr.insert(1,"James") ;
print("插入之后" + str(emptyArr));

''' 删除元素 START '''

print();
# 删除元素
# del
# del listName[index]
del emptyArr[1];
print(emptyArr);
print();

# pop() 删除最后一位元素
digitalList=["oneplus","mac","dell"];
pop_element = digitalList.pop();
print(digitalList);
print("被删除的元素 : " + pop_element) ;
print();

# pop(index) 删除特定位置的元素
digitalListTwo=["oneplus","mac","dell"];
pop_element_two = digitalListTwo.pop(2)
print(digitalListTwo) ;
print("被删除的元素 : " + pop_element_two) ;
print();

# remove
digitalListThree=["oneplus","mac","dell"];
digitalListThree.remove("123")

''' 删除元素 END '''
