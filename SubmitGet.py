import requests
import json

def Submit_Malware(filepath):
    # REST_URL = "http://111.68.99.39:8080/api/tasks/create/file/"
    SAMPLE_FILE = './Malware.txt'
    with open(SAMPLE_FILE, "rb") as sample:
        files = {"file": ("temp_file_name2", sample)}
        r = requests.post(filepath, files=files)
        return r
    task_id = r.json()
    # json_decoder = json.JSONDecoder()
    # task_id = json_decoder.decode(requests)["task_id"]
    #  task_id = json.loads(r)
    # print(r)
    task_ids=str(task_id)
    return task_ids
        # print type(task_id)


def get_report(task_id):
    REST_URL = "http://111.68.99.39:8080/api/tasks/get/report/"+str(task_id)+"/json"
    # SAMPLE_FILE = './Malware.txt'
    # with open(REST_URL, "rb") as sample:
    #      files = {"file": ("temp_file_name1", sample)}
    r = requests.get(REST_URL)
    # sr=r.content
    # print(sr)

    return r
    # for x, line in enumerate(r):
    #     if x==4:
    #         print(line)
    # r = requests.get(sample)
    # r.close()

response=get_report(16909)
print(response.text)

# SbMa=Submit_Malware("http://111.68.99.39:8080/api/tasks/create/file/")
# print(SbMa)