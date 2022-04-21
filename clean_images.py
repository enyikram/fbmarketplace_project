from PIL import Image
import glob
image_list = []
for filename in glob.glob("fbmarketplace_project/images/*.jpg"): 
    im=Image.open(filename)
    image_list.append(im)
