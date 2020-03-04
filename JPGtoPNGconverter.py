## Jpeg to Png converter
import sys
import os

from PIL import Image

## grab first and second args
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder, output_folder)

## check if new folder exists if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

## loop through folder and convert to png and
## save to new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    print(clean_name)
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('done!')


