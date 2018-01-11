def how_magicians(orgArr , targetArr):
    while orgArr:
        playerName = orgArr.pop()
        targetArr.append("the Greate " + playerName)

orgArr = ["Kobe" , "James" , "Irving"]
targetArr = []
how_magicians(orgArr,targetArr)

print("原始列表" + str(orgArr))
print("目标列表" + str(targetArr))


'''输出'''
'''
原始列表[]
目标列表['the Greate Irving', 'the Greate James', 'the Greate Kobe']
'''