import json
import re


today = []
yesterday = []
smaller_list_t = []
smaller_list_y = []

def getJSON(file, day):
    with open(file, 'r+') as fp:
        for line in fp:
            day.append(json.loads(line))
    return day

list_today = getJSON('./today.json', today)
list_yesterday = getJSON('./yesterday.json', yesterday)


for line in list_today[0:10]:
        try:
                if (line["mrp"] == "0") or (re.match("^\d+?\.\d+?$", line["mrp"]) is None) or (line["mrp"] == None):
                        line["mrp"] = "NA"
        except TypeError:
                line["mrp"] = "NA"
        smaller_list_t.append(line)

for line in list_yesterday[0:10]:
        try:
                if (line["mrp"] == "0") or (re.match("^\d+?\.\d+?$", line["mrp"]) is None) or (line["mrp"] == None):
                        line["mrp"] = "NA"
        except TypeError:
                line["mrp"] = "NA"
        smaller_list_y.append(line)

open("nmrp_today.json", 'a').close()
open("nmrp_yesterday.json", 'a').close()

with open("nmrp_today.json", "w") as f:
    json.dump(smaller_list_t, f)

with open("nmrp_yesterday.json", "w") as f:
    json.dump(smaller_list_y, f)

