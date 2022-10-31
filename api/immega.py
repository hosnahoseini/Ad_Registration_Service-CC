API_KEY = 'acc_dad6adae3ffdd9e'
API_SECRET = 'edbdcc05bdae358597325bc5023b0a75'
IMAGE_URL = 'https://wallpapercave.com/wp/wp3503654.jpg'

import requests

response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s' % IMAGE_URL,
    auth=(API_KEY, API_SECRET))

tags = response.json()['result']['tags']
for tag in tags:
  confidence = tag['confidence']
  tag_name = tag['tag']['en']
  print(f'Confidence: {confidence}, tag: {tag_name}')