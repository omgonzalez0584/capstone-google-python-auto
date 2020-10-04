#!/usr/bin/env python3
from PIL import Image
from subprocess import PIPE
import subprocess
import os
files = subprocess.run(['ls'], stdout=PIPE, stderr=PIPE)
files = files.stdout.decode().split()


for file in files:
        if not file.endswith('.py'):
                im = Image.open(file)
                new_im = im.rotate(90).resize((128,128)).convert("RGB")
                path = "/opt/icons/"+file
                new_im.save(path,"JPEG")
