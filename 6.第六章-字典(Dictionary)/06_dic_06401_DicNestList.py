aliens = []
for num in range(30):
    aliens.append({"name" : "alien"+str(num) , "country" : "Saab temple" , "color" : "green"})
for alien in aliens[:5]:
    print(alien)

print(str(len(aliens)))
