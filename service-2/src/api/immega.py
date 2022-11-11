import requests

API_KEY = 'acc_dad6adae3ffdd9e'
API_SECRET = 'edbdcc05bdae358597325bc5023b0a75'

def evaluate(image_url):
    response = requests.get(
          'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
           auth=(API_KEY, API_SECRET))

    tags = response.json()
    if tags:
      tags = tags['result']['tags']
    for tag in tags:
      confidence = tag['confidence']
      tag_name = tag['tag']['en']
      if tag_name == "vehicle" and confidence >= 50:
        return True
    return False
