import requests
import json
from bs4 import BeautifulSoup

REST_URL = "http://111.68.99.39:8080/api/tasks/get/report/1"
# SAMPLE_FILE = './Malware.txt'
# with open(REST_URL, "rb") as sample:
#      files = {"file": ("temp_file_name1", sample)}
r = requests.get(REST_URL)
print(r)
# plain_text=r.text
# soup=BeautifulSoup(plain_text,"html5lib")
# print(soup)
# for x, line in enumerate(r):
#     if x==4:
#         print(line)
    # r = requests.get(sample)
# r.close()


# import requests
#
# r = requests.post("http://111.68.99.39:8080/tasks/report/16810/", files=[
#     ("files", open(".\Malware.txt", "rb")),
#     ])
# # ("files", open("2.exe", "rb")),
# # r = requests.post('http://httpbin.org/post', data = {'key':'value'})
#
# # Add your code to error checking for r.status_code.
#
# submit_id = r.json()[1]
# task_ids = r.json()[2]
# errors = r.json()["errors"]