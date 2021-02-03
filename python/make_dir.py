import os
import glob

for i in glob.glob("*/"):
    if i[:3]=="abc" or i[:3]=="arc":
        os.rename(i,i.upper())

for i in range(1,200):
    for j in ("ABC","ARC"):
        os.makedirs(j+str(i).zfill(3),exist_ok=True)
