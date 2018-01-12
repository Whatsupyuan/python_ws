# 使用 ** 接受形参为 字典 类型的变量
# 传递参数时,要使用 key=value 的形式传递参数
def processInfo(firstName , **info):
    dicInfo = {}
    print(firstName)
    for key,value in info.items():
        dicInfo[key] = value
    return dicInfo
# key 的值为不带 双引号 , 否则报错
print(processInfo("yuan" , kobe="LA" , james="CLC" , lrving="bos"))


'''输出'''
'''
yuan
{'kobe': 'LA', 'james': 'CLC', 'lrving': 'bos'}
'''