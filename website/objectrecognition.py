import httplib, urllib, base64
import json
import sys

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '18b89d07773340b2887453e6d7fc36b1',
}

body = []

filepath = sys.argv[1]

with open(filepath, 'rb') as imageFile:
	image = imageFile.read()
	bytesArray = bytearray(image)
	body = bytesArray

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/tag", body, headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode('utf-8'))
    json_data = json.dumps(data, indent=4, default=lambda o: o.__dict__)	
    with open('tagged-images/image.json', 'w') as f:
		f.write(json_data) 
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))