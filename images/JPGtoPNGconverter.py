import sys
import os
import re
from PIL import Image

# grab arguments with sys
# argv1 Folder
# folder = sys.argv1
# new_folder = sys.argv2
folder = sys.argv[1]  # "filtered"
new_folder = sys.argv[2]  # "PNG_folder"
# argv2 new Folder
print(os.getcwd())
# os: check if folder exists
# os.path.isdir()
# or try to list images
try:
    files = os.listdir(f"{folder}/")
    # os.listdir(f"images/{new_folder}/")
except Exception as exc:
    print("Some folder not available: ", exc)

try:
    os.mkdir(f"images/{new_folder}")
except Exception as exc:
    print("error creating dir: ", exc)

JPGs = [filename for filename in files if re.search(r"[.]jpe?g$", filename)]
print(JPGs)
for file in JPGs:
    image = Image.open(f"{folder}/{file}")
    path = "images/" + new_folder + "/" + file.split('.')[0] + ".png"
    print("path: ", path)
    image.save(path)

print(JPGs)
