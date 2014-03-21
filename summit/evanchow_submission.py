import pandas as pd
from collections import defaultdict
import sys
import hashlib

products = defaultdict(str)
prodInfo = []
i = 0
with open('products_sample.csv') as f:
    for line in f:
        if i > 4:
            break
        print line.replace('\"', '')
        i += 1
        




#     for line in f:
#         code = hashlib.md5(line).hexdigest()[:6]
#         if products[code] is None:
#             products[code] = line.replace('\"', '')
#         else:
#             # rehash with sha-1
#             code = hashlib.sha1(line).hexdigest()[:6]
#             products[code] = line.replace('\"', '')
#         prodInfo.append((line.replace('\"', ''), code))

# for k, v in products.iteritems():
#     print k, v



# i = 0
# for (l, c) in prodInfo:
#     if i > 10:
#         break
#     print c, l.rstrip()
#     i += 1

# iCode = "c790d8"
# print products[iCode]