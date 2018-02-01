import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
webInfo = requests.get(url)
print("request status", webInfo.status_code)

response_dict = webInfo.json()
print("total_count:", response_dict["total_count"])
dict=response_dict["items"]
print("--")
for project in dict:
    print("project-name:", project["full_name"])
    print("stars-number:", project["stargazers_count"])
