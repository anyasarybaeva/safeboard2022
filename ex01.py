import json
from keyword import kwlist

json_f=input()
try:
    data = json.loads(json_f)
    result={}
    for key in data:
        if type(data[key]) in [list, tuple]:
            if len(data[key])==0:
                result[key]=[]
                continue
            for i in range(len(data[key])):
                new_key=key+"."+str(i)
                result[new_key]=data[key][i]
        elif type(data[key]) in [dict]:
            if len(data[key])==0:
                result[key]=[]
                continue
            for i in data[key]:
                new_key=key+"."+str(i)
                result[new_key]=data[key][i]
    res1=sorted(result.items())
    print(dict(res1))
except:
    print("{}")