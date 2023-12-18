from PIL import Image, ImageFilter
import tkinter as tk
from tkinter import filedialog

def apply_filter(image_path, output_path, filter_name):
    im = Image.open(image_path)
    if filter_name == 'Kelvin':
        # Tutaj możesz zastosować wybrany filtr zamiast BLUR
        im = im.filter(ImageFilter.BLUR)
    elif filter_name == 'Inkwell':
        im = im.filter(ImageFilter.CONTOUR)  # Przykładowe zastosowanie innego filtra
    # Dodaj warunki dla innych filtrów

    im.save(output_path)

def choose_file():
    filename = filedialog.askopenfilename()
    entry_file_path.delete(0, tk.END)
    entry_file_path.insert(0, filename)

def choose_output_folder():
    output_folder = filedialog.askdirectory()
    entry_output_path.delete(0, tk.END)
    entry_output_path.insert(0, output_folder)

def apply_selected_filter(filter_name):
    image_path = entry_file_path.get()
    output_path = entry_output_path.get()

    if image_path and output_path:
        apply_filter(image_path, output_path, filter_name)

root = tk.Tk()
root.title("Aplikacja przetwarzająca obrazy")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_choose_file = tk.Label(frame, text="Wybierz plik obrazu:")
label_choose_file.pack()

entry_file_path = tk.Entry(frame, width=50)
entry_file_path.pack()

button_browse_file = tk.Button(frame, text="Przeglądaj", command=choose_file)
button_browse_file.pack()

label_choose_output = tk.Label(frame, text="Wybierz miejsce zapisu:")
label_choose_output.pack()

entry_output_path = tk.Entry(frame, width=50)
entry_output_path.pack()

button_browse_output = tk.Button(frame, text="Przeglądaj", command=choose_output_folder)
button_browse_output.pack()

button_kelvin = tk.Button(frame, text="Kelvin", command=lambda: apply_selected_filter('Kelvin'))
button_kelvin.pack()

button_inkwell = tk.Button(frame, text="Inkwell", command=lambda: apply_selected_filter('Inkwell'))
button_inkwell.pack()

# Dodaj przyciski dla innych filtrów tutaj

root.mainloop()
