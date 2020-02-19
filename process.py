import PIL
from PIL import Image
import os
import os.path
import sys

# args
source_path = sys.argv[1]
dest_path = sys.argv[2]
if not os.path.exists(dest_path):
    os.makedirs(dest_path)

# const
valid_images = [".jpg", ".gif", ".png"]
new_size = int(sys.argv[3]) if len(sys.argv) > 3 else 500

for f in os.listdir(source_path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    image = Image.open(os.path.join(source_path, f))

    wpercent = (new_size / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((new_size, hsize), PIL.Image.ANTIALIAS)

    # image_name = 'processed_' + f
    image.save(os.path.join(dest_path, f))
