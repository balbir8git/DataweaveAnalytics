import json

today = []
yesterday = []
urlh_today = []
urlh_yesterday = []

def getJSON(file, day):
    with open(file, 'r') as fp:
        for line in fp:
            day.append(json.loads(line))
    return day

list_today = getJSON('./today.json', today)
list_yesterday = getJSON('./yesterday.json', today)

for item in list_today:
    urlh_today.append(item['urlh'])

for item in list_yesterday:
    urlh_yesterday.append(item['urlh'])

# print(len(urlh_today))
# print(len(urlh_yesterday))

overlapped_urlh = list(set(urlh_today).intersection(urlh_yesterday))
print(len(overlapped_urlh))


    
