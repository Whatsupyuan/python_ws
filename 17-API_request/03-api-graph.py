import requests
import matplotlib.pyplot as plt

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
webInfo = requests.get(url)
print("request status", webInfo.status_code)

response_dict = webInfo.json()
print("total_count:", response_dict["total_count"])
dict = response_dict["items"]
print("--")

names, star = [], []
for project in dict:
   names.append(project["full_name"])
   star.append(int(project["stargazers_count"]))

fig = plt.figure(dpi=128)
plt.bar(names,star)
plt.xlabel("",fontsize=9)
fig.autofmt_xdate()
plt.show()