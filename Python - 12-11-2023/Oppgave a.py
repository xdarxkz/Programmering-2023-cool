from PIL import Image
import pilgram

im = Image.open('bilder/chicken.jpg')
pilgram.kelvin(im).save('sample-kelvin.jpg')