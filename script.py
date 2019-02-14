import json
from collections import Counter

today = []
yesterday = []
urlh_today = []
urlh_yesterday = []
categories_today = []
categories_yesterday = []
subcat_today = []
subcat_yesterday = []

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
    subcat_today.append(item['subcategory'])

for item in list_yesterday:
    urlh_yesterday.append(item['urlh'])
    categories_yesterday.append(item['category'])
    subcat_yesterday.append(item['subcategory'])

# print(len(urlh_today))
# print(len(urlh_yesterday))

overlapped_urlh = list(set(urlh_today).intersection(urlh_yesterday))
print("1. No. of overlapped urlh: ", len(overlapped_urlh))

# print("categories today: ", len(set(categories_today)))
# print("categories yesterday: ", len(set(categories_yesterday)))

categories_unique = set(categories_today).intersection(categories_yesterday)
print("3. No. of unique categories in both files: ", len(categories_unique))

categories_total = categories_today + categories_yesterday
print("4. List of categories which is not overlapping: ", list(set(categories_total).difference(categories_unique)))


subcat_set = set(subcat_today).intersection(subcat_yesterday)
subcat_total = subcat_today + subcat_yesterday
list_total = list_today + list_yesterday
subcat_total = subcat_today + subcat_yesterday
subcat_dict = Counter(subcat_total)

print("5. Taxonomies: ")
for line in list_total:
    if line['category'] in categories_unique and line['subcategory'] in subcat_set:
        print(line['category'] + " > " + line['subcategory'] + ": " + str(subcat_dict[line['subcategory']]))
        subcat_set.remove(line['subcategory'])
