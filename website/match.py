import json
import numpy as np
with open('databaseArt.json') as json_data:
    data = json.load(json_data)

with open('image.json') as json_data:
    things = json.load(json_data)

max = -1
descriptionOfMax = ''
for item in data:
    if 'tags' in item.keys() and  'description' in item.keys():
        a = np.intersect1d(item['tags'],things)
        if len(a) > max:
            max = len(a)
            descriptionOfMax = item['description']

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
with open('rnn/art.txt', 'w') as outfile:
  outfile.write(" ".join(data))

