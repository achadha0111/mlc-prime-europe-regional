import json
import numpy as np
import random

with open('databaseArt.json') as json_data:
    data = json.load(json_data)

with open('tagged-images/image.json') as json_data:
    things = json.load(json_data)

max_hits = -1
descriptionOfMax = ''
for item in data:
    if 'tags' in item.keys() and  'description' in item.keys():
        a = np.intersect1d(item['tags'],things)
        if len(a) > max_hits:
            max_hits = len(a)
            descriptionOfMax = item['description']

if (max_hits == 0):
   descriptionIndex = random.randint(1, len(data))
   descriptionOfMax = data[descriptionIndex]['description']

delimiters = ['\n', ' ', ',', '.', '?', '!', ':']
length = 0
seed = ''
for c in descriptionOfMax:
    seed += c
    length += 1
    if c in delimiters and length > 100:
        break

data =[]
data.append(seed)
return data[0].encode('ascii', 'ignore')


