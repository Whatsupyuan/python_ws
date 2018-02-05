a = 'alex'
b = a.title()
c = a.capitalize()
print(b)
print(c)

name = 'alex'
print(name.strip())
print(name.startswith("al"))
print(name.endswith("x"))
print(name.replace("l", "p"))
print(name.split("l"))
print(name.upper())
print(name.lower())
print(name[1])
print(name[0:2])
print(name[2:4])
print(name.index("e"))
print(name.find("e"))
print(name[0:len(name) - 1])

# interate string value
print("interate string\n")
for val in name:
    print(val)

print("\n")

li = "alexericrain"
v = "_".join(li)
print(v)

print()

li = ["a","b","c"]
v = "-".join(li)
print(v)
print()

print()
print("123/3".find("+"))