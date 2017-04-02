#!/usr/bin/python
import clarifai
from clarifai.rest import ClarifaiApp
import sys
import json

app = ClarifaiApp("FTWDbLfHgAzJU2Bwax1uhopFOZ854Xz5xI3C9HG5", "C3x_RcA0XU3yBGmqY8Lu3SkOkA7ga9Llzczs0KEI")
filename = sys.argv[1]
concepts = []

model = app.models.get("general-v1.3")
dataJSON = model.predict_by_filename(filename)
for output in dataJSON['outputs']:
	for concept in output['data']['concepts']:
		concepts.append(concept['name'])

with open('image.json', 'a') as f:
        f.write(concepts) 

