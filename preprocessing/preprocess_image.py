import cv2

def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Normalize brightness and contrast
    normalized_image = cv2.normalize(gray_image, None, 0, 255, cv2.NORM_MINMAX)
    
    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(normalized_image, (5, 5), 0)
    
    # Apply thresholding to create a binary image
    _, thresholded_image = cv2.threshold(blurred_image, 100, 255, cv2.THRESH_BINARY)
    
    # Save the processed image
    cv2.imwrite('../output/preprocessed_image.jpg', thresholded_image)
    
    return thresholded_image

if __name__ == '__main__':
    preprocess_image('../output/product_image.jpg')
