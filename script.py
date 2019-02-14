import json
import re
from collections import Counter

today, yesterday, urlh_today, urlh_yesterday, categories_today, categories_yesterday = ([] for i in range(6))


def getJSON(file, day):
    with open(file, 'r+') as fp:
        for line in fp:
            day.append(json.loads(line))
    return day

subcat_today, subcat_yesterday = [], []
list_today = getJSON('./today.json', today)
list_yesterday = getJSON('./yesterday.json', yesterday)

for item in list_today:
    urlh_today.append(item['urlh'])
    categories_today.append(item['category'])
    subcat_today.append(item['subcategory'])

for item in list_yesterday:
    urlh_yesterday.append(item['urlh'])
    categories_yesterday.append(item['category'])
    subcat_yesterday.append(item['subcategory'])

overlapped_urlh = list(set(urlh_today).intersection(urlh_yesterday))
print("1. No. of overlapped urlh: ", len(overlapped_urlh))

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

valid_list_today = []
valid_list_yesterday = []

for i in range(len(list_today)):
    if list_today[i]['http_status'] == "200":
        valid_list_today.append(list_today[i])

for j in range(len(list_yesterday)):
    if list_yesterday[j]['http_status'] == "200":
        valid_list_yesterday.append(list_yesterday[j])

set_overlapped_urlh = set(overlapped_urlh)

print("2. Price differnces: ")

for line_t in valid_list_today[0:10000]:
    for line_y in valid_list_yesterday[0:10000]:
        if line_t['urlh'] == line_y['urlh'] and line_t['urlh'] in set_overlapped_urlh:
            temp1 = line_t['available_price']
            temp2 = line_y['available_price']
            if temp1 != None and temp2 != None:
                temp1 = float(temp1)  
                temp2 = float(temp2)
                if (type(temp1) == 'int' or type(temp1 == 'float')) and (type(temp2) == 'int' or type(temp2 == 'float')):
                    if temp1 != temp2:
                        print("%.2f" %abs(temp1-temp2))                        
                        set_overlapped_urlh.remove(line_t['urlh'])
            break

print("------------------------------------------")
print("NOTE: Output of section(2) has been made smaller(10000 elements) so that viewer can have a better look at outputs.")
print("Solution of section is in different file (mrp.py) because it generates files.")