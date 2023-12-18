from PIL import Image

def rotate_clockwise(image):
    return image.rotate(-90, expand=True)

def rotate_counter_clockwise(image):
    return image.rotate(90, expand=True)

def rotate_180(image):
    return image.rotate(180, expand=True)

def main():
    im = Image.open('bilder/eple.jpg')

    print("Velg en rotasjon:")
    print("1. 90 grader med klokka")
    print("2. 90 grader mot klokka")
    print("3. 180 grader")
    choice = input("Skriv inn nummeret for ønsket rotasjon: ")

    if choice == '1':
        rotated_image = rotate_clockwise(im)
    elif choice == '2':
        rotated_image = rotate_counter_clockwise(im)
    elif choice == '3':
        rotated_image = rotate_180(im)
    else:
        print("Ugyldig valg.")

    if 'rotated_image' in locals():
        rotated_image.save('rotated_image.jpg')
        print("Bildet er rotert og lagret som 'rotated_image.jpg'.")

if __name__ == "__main__":
    main()
