import json

today = []
yesterday = []
urlh_today = []
urlh_yesterday = []
categories_today = []
categories_yesterday = []

def getJSON(file, day):
    with open(file, 'r') as fp:
        for line in fp:
            day.append(json.loads(line))
    return day

list_today = getJSON('./today.json', today)
list_yesterday = getJSON('./yesterday.json', today)

for item in list_today:
    urlh_today.append(item['urlh'])
    categories_today.append(item['category'])

for item in list_yesterday:
    urlh_yesterday.append(item['urlh'])
    categories_yesterday.append(item['category'])

# print(len(urlh_today))
# print(len(urlh_yesterday))

overlapped_urlh = list(set(urlh_today).intersection(urlh_yesterday))
print("1. No. of overlapped urlh: ", len(overlapped_urlh))

# print(len(set(categories_today)))
# print(len(set(categories_yesterday)))

print("3. No. of unique categories in both files: ", len(set(categories_today).intersection(categories_yesterday)))
