Simple Analytics Program:
-------------------------

Given two JSON files (y.json, t.json), write a small analytics program to perform the following:

1. No of URLH which are overlapping.

2. For all the URLH which are overlapping, calculate the price difference (wrt available_price) if there is any between yesterday's and today's crawls. There might be duplicate URLHs in which case you can choose the first valid (with http_status 200) record.

3. No of Unique categories in both files.

4. List of categories which is not overlapping.

5. Generate the stats with count for all taxonomies (taxonomy is concatenation of category and subcategory separated by " > ").
Eg:
Cat1 > Subcat1: 3500
Cat1 > Subcat2: 2000
Cat2 > Subcat3: 8900

6. Generate a new file where mrp is normalized. If there is a 0 or a non-float value or the key doesn't exist, make it "NA".
