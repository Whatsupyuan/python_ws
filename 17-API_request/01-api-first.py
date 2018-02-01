import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
webInfo = requests.get(url)
print("request status" , webInfo.status_code)

response_dict = webInfo.json()
for key in response_dict.keys():
    print(key)