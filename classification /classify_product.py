import cv2
import numpy as np
from tensorflow.keras.models import load_model

def classify_product(image_path, model_path):
    # Load the trained model
    model = load_model(model_path)
    
    # Load and preprocess the image
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (64, 64))
    image_array = np.array(image_resized).reshape(1, 64, 64, 3)
    image_array = image_array / 255.0  # Normalize the image
    
    # Predict the class (fresh/defective)
    prediction = model.predict(image_array)
    
    if prediction > 0.5:
        print("Product is fresh or passes quality check.")
    else:
        print("Product is defective or expired.")

if __name__ == '__main__':
    classify_product('../output/preprocessed_image.jpg', '../output/cnn_model.h5')
