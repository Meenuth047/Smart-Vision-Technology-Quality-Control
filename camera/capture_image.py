import cv2
import os

def capture_image():
    # Define the output directory path relative to the current script location
    output_dir = "../output"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the camera (0 for default camera)
    cap = cv2.VideoCapture(0)
    
    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None
    
    # Capture a frame
    ret, frame = cap.read()
    
    if ret:
        # Save the captured image in the output folder
        image_path = os.path.join(output_dir, 'product_image.jpg')
        cv2.imwrite(image_path, frame)
        print(f"Image captured and saved successfully at: {image_path}")
    else:
        print("Error: Failed to capture image.")
    
    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_image()
