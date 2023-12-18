from PIL import Image

def main():
    im = Image.open('bilder/eple.jpg')

    print(f"Opprinnelig størrelse: {im.size}")

    if im.width < 1080:
        ny_bredde = 1080
        ny_hoyde = int(im.height * (ny_bredde / im.width))
        im = im.resize((ny_bredde, ny_hoyde))

        print(f"Endret størrelse: {im.size}")
        im.save('resized_image.jpg')
        print("Bildet er endret i størrelse og lagret som 'resized_image.jpg'.")
    else:
        print("Bildet oppfyller allerede minimumskravet til Instagram.")

if __name__ == "__main__":
    main()
