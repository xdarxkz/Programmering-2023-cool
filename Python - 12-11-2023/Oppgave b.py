from PIL import Image
import pilgram

im = Image.open('bilder/eple.jpg')
pilgram.inkwell(im).save('sample-inkwell.jpg')