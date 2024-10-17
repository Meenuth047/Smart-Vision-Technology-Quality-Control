from camera.capture_image import capture_image
from preprocessing.preprocess_image import preprocess_image
from feature_extraction.extract_text_ocr import extract_text_from_image
from feature_extraction.detect_defects import detect_defects
from classification.classify_product import classify_product

def main():
    # Step 1: Capture Image
    print("Capturing product image...")
    capture_image()

    # Step 2: Preprocess Image
    print("Preprocessing image...")
    preprocess_image('../output/product_image.jpg')

    # Step 3: Feature Extraction
    print("Extracting text from image using OCR...")
    extract_text_from_image('../output/preprocessed_image.jpg')
    
    print("Detecting defects in the product...")
    detect_defects('../output/preprocessed_image.jpg')

    # Step 4: Classification
    print("Classifying the product (fresh/defective)...")
    classify_product('../output/preprocessed_image.jpg', '../output/cnn_model.h5')

if __name__ == '__main__':
    main()
