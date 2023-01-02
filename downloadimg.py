import subprocess
import wget
import requests
import ast
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import shutil
import os

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
r = requests.get(url,params = {"hd": "True"})

data = ast.literal_eval(r.content.decode('utf-8'))
title = data["title"]
print(title)
print(data["url"])
name = wget.download(data["url"])
destination = f"aster-wallpaper/usr/share/backgrounds/asterlinux/{title}.jpg"
shutil.move(name,destination)
