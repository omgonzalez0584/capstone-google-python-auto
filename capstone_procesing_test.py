#! /usr/bin/env python3

import os
import requests
import json

files = os.listdir('/data/feedback')
feed_dict =  {}


for file in files:
    with open('/data/feedback/'+file) as f:
        lines = f.readlines()
        feed_dict['title'] = lines[0].strip()
        feed_dict['name'] = lines[1].strip()
        feed_dict['date'] = lines[2].strip()
        feed_dict['feedback'] = lines[3].strip()
        print(feed_dict)
        response = requests.post("http://35.223.101.86/feedback/",json=feed_dict)
        print(response.status_code)
