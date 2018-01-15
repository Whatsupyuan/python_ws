fileName = "1.txt"
with open(fileName) as file:
    for line in file:
        print(line.rstrip())
