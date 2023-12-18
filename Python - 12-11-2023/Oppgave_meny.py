import argparse, pilgram
from PIL import Image

print("Bra jobba!")


def kelvin_filter(image_path, output_path):
    im = Image.open(image_path)
    pilgram.kelvin(im).save(output_path)

def inkwell_filter(image_path, output_path):
    im = Image.open(image_path)
    pilgram.inkwell(im).save(output_path)

def rotate_clockwise(image_path, output_path):
    im = Image.open(image_path)
    rotated_image = im.rotate(-90, expand=True)
    rotated_image.save(output_path)

def rotate_counter_clockwise(image_path, output_path):
    im = Image.open(image_path)
    rotated_image = im.rotate(90, expand=True)
    rotated_image.save(output_path)

def rotate_180(image_path, output_path):
    im = Image.open(image_path)
    rotated_image = im.rotate(180, expand=True)
    rotated_image.save(output_path)

def resize_for_instagram(image_path, output_path):
    im = Image.open(image_path)
    if im.width < 1080:
        new_width = 1080
        new_height = int(im.height * (new_width / im.width))
        resized_image = im.resize((new_width, new_height))
        resized_image.save(output_path)
    else:
        print("Bildet oppfyller allerede minimumskravet til Instagram.")

def pixelate(image_path, output_path, scale=5):
    image = Image.open(image_path)
    image = image.resize((image.size[0] // scale, image.size[1] // scale), Image.NEAREST)
    image = image.resize((image.size[0] * scale, image.size[1] * scale), Image.NEAREST)
    image.save(output_path)

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image Processing CLI')
    parser.add_argument('image_path', help='bilder/men.png')
    parser.add_argument('output_path', help='New saved image.png')
    parser.add_argument('-f', '--function', help='Choose a function: kelvin, inkwell, rotate_clockwise, rotate_counter_clockwise, rotate_180, resize_for_instagram, pixelate, add_polaroid_frame')

    args = parser.parse_args()

    if args.function == 'kelvin':
        kelvin_filter(args.image_path, args.output_path)
    elif args.function == 'inkwell':
        inkwell_filter(args.image_path, args.output_path)
    elif args.function == 'rotate_clockwise':
        rotate_clockwise(args.image_path, args.output_path)
    elif args.function == 'rotate_counter_clockwise':
        rotate_counter_clockwise(args.image_path, args.output_path)
    elif args.function == 'rotate_180':
        rotate_180(args.image_path, args.output_path)
    elif args.function == 'resize_for_instagram':
        resize_for_instagram(args.image_path, args.output_path)
    elif args.function == 'pixelate':
        pixelate(args.image_path, args.output_path)
    elif args.function == 'add_polaroid_frame':
        frame_path = 'bilder/polaroid.png' 
        add_polaroid_frame(args.image_path, frame_path, args.output_path)
    else:
        print('Invalid function name. Please choose from the available functions.')
