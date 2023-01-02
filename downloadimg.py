#    Wallpaper Download application via NASA image api 
#    made for Aster Wallpaper packge

import subprocess
import wget
import requests
import ast
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import shutil
import os

user_date = "2022-12-31"
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# uncomment to download a specific date
#r = requests.get(url,params = {"hd": "True","date": d})

# Downloads daily images
r = requests.get(url,params = {"hd": "True"})

# makes api request accessable
data = ast.literal_eval(r.content.decode('utf-8'))

# set an title
title = data["title"].replace(" ","_").replace(":","_")
print(title)

# name of the downloaded image
print(data["url"])
name = wget.download(data["url"])

# Destination of the finel image and rename it
destination = f"aster-wallpaper/usr/share/backgrounds/asterlinux/{title}.jpg"

# Copy to ureviciouly asined path
shutil.move(name,destination)

