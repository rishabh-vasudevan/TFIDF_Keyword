import csv
import json
import ast 
from operator import itemgetter


inv_list = {}
inv_list_final={}
inv_list_with_one_keyword={}
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
        v = list(filter(lambda x: x[1]>0, v))
        if len(v)>0:
          inv_list_final[k] = sorted(v, key = itemgetter(1), reverse=True)
    else:
      if len(v)>0:
        inv_list_with_one_keyword[k] = v

with open('inverted_list.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(inv_list_final.items())

with open('inverted_list_with_one_word.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(inv_list_with_one_keyword.items())
    
## Double inverting the list

double_inverted_list = {}
for k,v in inv_list_final.items():
  for coin in v:
    if coin[0] not in double_inverted_list:
      double_inverted_list[coin[0]] = []
    double_inverted_list[coin[0]].append((k,coin[1]))

with open('double_inverted_list.csv', 'w') as f:
    w = csv.writer(f)
    w.writerows(double_inverted_list.items())
