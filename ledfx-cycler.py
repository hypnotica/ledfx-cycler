#!/usr/bin/env python3

import time
import sys
import requests

seconds_per_scene = 30
scenes_url = "http://127.0.0.1:8888/api/scenes"
scenes = requests.get(scenes_url)
scenes.raise_for_status()
scenes_dict = scenes.json()

if len(sys.argv) >= 2 and sys.argv[1].isdigit():
    seconds_per_scene = sys.argv[1]

if len(sys.argv) >= 3:
    scenes_url = sys.argv[2]

if scenes_dict["status"] == "success":
    try:
        while True:
            for scene in scenes_dict["scenes"]:
                req = requests.put(scenes_url, json={'id': str(scene), 'action': 'activate'})
                time.sleep(seconds_per_scene)
    except KeyboardInterrupt:
        exit
