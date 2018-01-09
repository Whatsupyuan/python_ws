aliens = []
for num in range(30):
    aliens.append({"name" : num , "color" : "black"})

print(aliens)

# 此处 Java 不一样，截取 list 0-3 中不是新建的对象，而是原aliens list 进行的修改
# 需要多使用理解不同
for alien in aliens[0:3]:
    alien["color"] = "blue"

print()
print(aliens)



# dic 中嵌套list
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name,languages in favorite_languages.items():
    print(name)
    for lang in languages:
        print(lang)