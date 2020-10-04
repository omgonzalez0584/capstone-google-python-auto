#!/usr/bin/env python3
from PIL import Image
from subprocess import PIPE
import subprocess
import os
files = subprocess.run(['ls'], stdout=PIPE, stderr=PIPE)
files = files.stdout.decode().split()

os.mkdir("new_images")
print(os.getcwd())
for file in files:
    if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.webp'):
        im = Image.open(file)
        new_im = im.rotate(90).resize((128,128)).convert("RGB")
        new_im.save(file,"JPEG")
