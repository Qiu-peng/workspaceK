# a = '2016-11-25'
# l = list(a)
# l9 = l[9]
# l8 = l[8]
# l5 = l[5]
# l6 = l[6]
# if l8 != '3' and l9 == '9':
#     l[8] = str(int(l[8]) + 1)
#     l[9] = '0'
# elif l8 != '3':
#     l[9] = str(int(l[9])+1)
# elif l8 == '3' and l9 == '0':
#     l[8] = '3'
#     l[9] = '0'
# elif l8 == '3' and l9 == '1':
#     l[8] = '3'
#     l[9] = '1'
# else:
#     l[8] = '3'
#     l[9] = '0'
# new = ''.join(l)
# print(new)

# print([x for x in range(2,10,2)])
# import datetime
# times = datetime.datetime.now()
# print(times)

# import re

# a = "[112,2,399,4,5]"
# r = '[[\\]"]'
# line = re.sub(r, '', a)
# s = line.split(",")
# print(type(s))
# print(s)
# b = ["112", "2", "3", "7"]
# s = [1, 2, 3]
# ss = [str(i) for i in s]


# print([l for l in ss if l not in b])
# print([l for l in b if l not in ss])
# for i in s:
#     print(i)
# print(type(line))
# print(line)
# from datetime import date, datetime
# import time
# s = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
# print(s)
import json
# inoutdatas = {
#     "records": [
#         {"RECORDID": "SZAKT-4156451",
#          "TYPE": 0,
#          "SJ": "2017-12-06 17:43:43",
#          "XZQH": "雨花区",
#          "SSFXSJDM": "430111000000",
#          "SSFXSJMC": "雨花分局",
#          "SSPCSDM": "430111470000",
#          "SSPCSMC": "圭塘派出所",
#          "TCC": "汇远大厦",
#          "CLHP": "临A2JA13",
#          "INFO": {"TCCXX": {"TCCDZ": "雨花区劳动东路5号"}}
#          }
#     ]
# }
# inoutdatas = json.dumps(inoutdatas)
# print(inoutdatas)

inp_strr = '{"k1":123, "k2": "456", "k3":"ares"}'
inp_dict = json.loads(inp_strr) # 根据字符串书写格式，将字符串自动转换成 字典类型
print(inp_dict)
print(type(inp_dict))
print(inp_dict["k1"])
