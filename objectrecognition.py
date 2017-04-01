import httplib, urllib, base64
import json

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '18b89d07773340b2887453e6d7fc36b1',
}

body = "{'url':'https://images-na.ssl-images-amazon.com/images/G/01/img15/pet-products/small-tiles/23695_pets_vertical_store_dogs_small_tile_8._CB312176604_.jpg'}"

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/tag", body, headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode('utf-8'))
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))