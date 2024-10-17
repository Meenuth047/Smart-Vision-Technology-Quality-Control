import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    # Open the image using PIL
    image = Image.open(image_path)
    
    # Use Tesseract to extract text
    extracted_text = pytesseract.image_to_string(image)
    
    print("Extracted Text:", extracted_text)
    return extracted_text

if __name__ == '__main__':
    extract_text_from_image('../output/preprocessed_image.jpg')
