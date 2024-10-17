import cv2

def detect_defects(image_path):
    # Load the preprocessed image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use Canny Edge Detection to find edges
    edges = cv2.Canny(gray, 100, 200)
    
    # Find contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw the contours
    result = image.copy()
    cv2.drawContours(result, contours, -1, (0, 255, 0), 2)
    
    # Save the image with drawn contours
    cv2.imwrite('../output/defect_detected_image.jpg', result)
    
    return result

if __name__ == '__main__':
    detect_defects('../output/preprocessed_image.jpg')
