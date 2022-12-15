import csv
import json
import ast 
from operator import itemgetter


inv_list = {}
inv_list_final={}
with open('keywords.csv') as kw_file:
  for line in kw_file:
    kwlist = line.split(',')
    coin = kwlist[0]
    kws_str = ','.join(kwlist[1:])
    kws_json_str = json.loads(kws_str)
    kws_json = ast.literal_eval(kws_json_str)
    for kw in kws_json:
      if kw[0] not in inv_list:
        inv_list[kw[0]] = []
      inv_list[kw[0]].append((coin,kw[1]))

  for k, v in inv_list.items():
    if len(v) > 1:
        inv_list_final[k] = sorted(v, key = itemgetter(1), reverse=True)

with open('inverted_list.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(inv_list_final.items())