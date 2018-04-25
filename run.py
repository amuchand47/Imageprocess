from glob import glob
from PIL import Image
import cv2
import os

f = glob('./*.png')

c = 1

for j in f:
    img = Image.open(j).convert('L')
    img.save('output_file'+str(c)+'.jpg')
    c = c+1

pngs = glob('./*.png')
for i in pngs:
    os.remove(i)