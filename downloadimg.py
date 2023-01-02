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
print(data["url"])
name = wget.download(data["url"])
print (name)
destination = f"aster-wallpaper/usr/share/backgrounds/asterlinux/{name}"
shutil.move(name,destination)
