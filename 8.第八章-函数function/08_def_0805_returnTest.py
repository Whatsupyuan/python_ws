# 8-6
def city_country(city , country , songs=""):
    print(city + "," + country)
city_country("Beijing","China" , "01-Cross")
city_country("LA","American")
city_country("CLC","American")

# 8-7
def make_album(singer , albumName):
    return {singer : albumName}
def make_album2(singer , albumName):
    dic = {}
    dic[singer] = albumName
    return dic

a1 = make_album("akon" , "will")
a2 = make_album("Lady","Proker Face")
a3 = make_album2("akon" , "will")
a4 = make_album2("Lady","Proker Face")
print(a1)
print(a2)
print(a3)
print(a4)

# 8-9
flag = True
while flag:
    albumInfo = {}
    albumName = input("Please input your album name,If want exit please input 'q'")
    singer = input("Please input your singer name,If want exit please input 'q'")
    if albumName == 'q' or singer == 'q':
        break
    albumInfo = make_album2(singer,albumName)
    print(albumInfo)