from PIL import Image

def add_polaroid_frame(image_path, frame_path, output_path):

    image = Image.open(image_path)
    frame = Image.open(frame_path)
    
    width, height = image.size
    min_dimension = min(width, height)
    cropped_image = image.crop(((width - min_dimension) // 2, (height - min_dimension) // 2, 
                                (width + min_dimension) // 2, (height + min_dimension) // 2))
    
    scaled_image = cropped_image.resize((760, 760), Image.LANCZOS)

    canvas = Image.new('RGB', frame.size)

    canvas.paste(scaled_image, (64, 64))
    
    canvas.paste(frame, (0, 0), frame)
    
    canvas.save(output_path)

image_path = 'bilder/men.png'
frame_path = 'bilder/polaroid.png'
output_path = 'saved photo polaroid.jpg'

add_polaroid_frame(image_path, frame_path, output_path)
