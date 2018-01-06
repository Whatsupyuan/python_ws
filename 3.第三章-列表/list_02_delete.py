'''
数组操作 CURD

添加 : append(value);
插入元素 : insert(targetIndex , value);

删除:
根据Index删除: del , pop
根据值删除 : remove(value);
'''
''' 删除元素 START '''
# remove
# 如果删除的 value 不在 list 中,则会报错
# remove 删除list中多个相同值时无法删除 , 只能删掉第一次出现该值的元素
digitalListThree=["oneplus","mac","dell" , "mac"];
# digitalListThree.remove("123");
digitalListThree.remove("mac");
print(digitalListThree) ;

''' 删除元素 END '''
