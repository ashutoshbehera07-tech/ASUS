import cv2
import pytesseract
import googletrans
import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk

# function for detecting the text (currently a placeholder)
def detect_text(image):
    return []  # Placeholder function for text detection

# function for extracting text regions (currently a placeholder)
def extract_text_regions(image, boxes):
    return []  # Placeholder for extracting regions of text

# function for character recognition using pytesseract
def recognizing_text(image, lang='eng'):
    text = pytesseract.image_to_string(image, lang=lang)
    return text

# function for translating the text to the desired language using googletrans
def translating_text(text, desired_lang):
    translator = googletrans.Translator()
    try:
        translated_text = translator.translate(text, dest=desired_lang)  # Fixed the 'dest' keyword
        return translated_text.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return "Translation error."

# function for processing the image, recognize the text, translate the text and store the resulting text
def processing_image():
    image_path = filedialog.askopenfilename()  # Opening file dialog to select image
    
    image = cv2.imread(image_path)  # Loading the image using OpenCV

    if image is None:
        print("Error: Unable to load image.")
        return

    show_image(image_path)

    boxes = detect_text(image)  # Performing the text detection (currently empty)

    text_regions = extract_text_regions(image, boxes)  # Extract text regions (currently empty)

    recognized_text = recognizing_text(image)  # Performing the character recognition from the image
    
    if recognized_text.strip():  # Check if any text was recognized
        selected_language = languages[lang_choice.get()]  # Get the selected language from the dropdown
        translated_text = translating_text(recognized_text, selected_language)

        # Store extracted and translated text
        text_strorage.append({'Extracted': recognized_text, 'Translated': translated_text})

        update_text_storage_display()
    else:
        print("No text found in the image.")

def show_image(image_path):
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((200,200))

    tk_image = ImageTk.PhotoImage(pil_image)

    image_label.config(image=tk_image)
    image_label.image = tk_image

def update_text_storage_display():
    storage_text.delete('1.0', tk.END)
    for idx, item in enumerate(text_strorage, start=1):
        storage_text.insert(tk.END, f"Text {idx}:\nExtracted: {item['Extracted']}\nTranslated: {item['Translated']}\n\n")

# Tkinter GUI setup
window = tk.Tk()
window.title("OCR and Translated Text")
window.geometry("1000x800")
window.configure(background='blue')

# Browse button to select image
browse_button = tk.Button(window, text="Browse Image", command=processing_image)
browse_button.pack(pady=10)

# Dropdown menu for language selection
languages = {
    'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar',
    'English': 'en', 'French': 'fr', 'German': 'de', 'Hindi': 'hi',
    'Italian': 'it', 'Japanese': 'ja', 'Portuguese': 'pt', 'Spanish': 'es',
    'Chinese (Simplified)': 'zh-cn', 'Chinese (Traditional)': 'zh-tw', 'Russian': 'ru'
}

lang_choice = tk.StringVar(window)
lang_choice.set('English')  # Default to English
language_menu = tk.OptionMenu(window, lang_choice, *languages.keys())
language_menu.pack(pady=5)

image_label = tk.Label(window)
image_label.pack(pady=10)


# Text storage to display extracted and translated text
text_strorage = []

storage_text = tk.Text(window, width=100, height=50)
storage_text.pack(pady=10)

# Run the Tkinter main loop
window.mainloop()

