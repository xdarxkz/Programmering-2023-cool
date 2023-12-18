from PIL import Image

def pixelate(image_path, output_path, scale=5):

    image = Image.open(image_path)
    

    image = image.resize((image.size[0] // scale, image.size[1] // scale), Image.NEAREST)
    image = image.resize((image.size[0] * scale, image.size[1] * scale), Image.NEAREST)

    image.save(output_path)


image_path = 'bilder/men.png'
output_path = 'pixelated_image.jpg'

pixelate(image_path, output_path)
