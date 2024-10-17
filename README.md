# Smart-Vision-Technology-Quality-Control
Smart vision technology to use advanced imaging systems and algorithms to capture and analyze visual information. In the context of quantity and quality testing, it helps automate the quality inspection process by identifying a product, its quantity and any defects or quality attributes.

How to Run the Project

1. Set up the environment: Install dependencies using the following command:
    pip install -r requirements.txt
2. Train the CNN model (if not pre-trained): Run the model training script:
   python classification/train_model.py
3. Capture an Image: Run the following to capture a product image:
   python camera/capture_image.py
4. Preprocess the Image: Preprocess the captured image:
   python preprocessing/preprocess_image.py
5. Extract Features and Classify: Run the main script to preprocess, extract features, and classify the product:
   python main.py

**Folder Setup Process**

  **Camera Setup:**
        File: /camera/capture_image.py
        Function: Captures a new image of the product for processing.

**  Preprocessing:**
        File: /preprocessing/preprocess_image.py
        Function: Preprocesses the image by converting it to grayscale, normalizing brightness and contrast, and applying filters like Gaussian blur.
**
  Feature Extraction:**
        File: /feature_extraction/extract_text_ocr.py
        Function: Extracts text like expiry date, product name, and other information from the image using Tesseract OCR.
        File: /feature_extraction/detect_defects.py
        Function: Detects any defects in the product’s packaging or physical appearance using edge detection.

  **Classification:**
        File: /classification/cnn_model.py
        Function: Defines the Convolutional Neural Network (CNN) model for classifying images.
        File: /classification/train_model.py
        Function: Trains the CNN model using the dataset of product images stored in the /data/training_data/ folder.
        File: /classification/classify_product.py
        Function: Uses the trained model to classify a product as fresh/defective based on the captured image.

 ** Main Script:**
        File: /main.py
        Function: This script coordinates the entire process, from capturing the image to classifying the product.
        
**Explanation of the Structure**

  /camera: This folder contains the script to capture images from the camera.
        capture_image.py: This file captures an image using a webcam and saves it to the /output folder as product_image.jpg.

  /preprocessing: This folder contains the image preprocessing script.
        preprocess_image.py: This script preprocesses the captured image (grayscale, normalization, and thresholding) and saves the output as preprocessed_image.jpg in the /output folder.

  /feature_extraction: This folder contains the scripts for OCR text extraction and defect detection.
        extract_text_ocr.py: Uses Tesseract to extract text such as product names, expiry dates, and other packaging details.
        detect_defects.py: Performs edge detection and contour analysis to identify physical defects in the product and saves the result as defect_detected_image.jpg in the /output folder.

   /classification: This folder contains scripts related to the CNN model for classifying products.
        cnn_model.py: Defines the CNN model architecture for classifying whether a product is fresh or defective.
        train_model.py: Contains the code to train the CNN model using the images in the /data/training_data folder.
        classify_product.py: Uses the trained model to classify an image of a product as fresh or defective.

  /data: This folder holds training and testing datasets.
        /training_data: Contains subfolders for different classes of product images (e.g., fresh and expired). This folder is used for training the CNN model.
        /test_images: Contains images captured during the actual test, which are processed and classified.

  /output: This folder stores the outputs of various stages like the captured image, preprocessed image, and images with defects detected.

  main.py: This is the main script that ties everything together. It will:
        Capture an image from the camera.
        Preprocess the image.
        Perform feature extraction (OCR and defect detection).
        Classify the product using the trained CNN model.
        Display real-time feedback on whether the product is accepted or rejected.

  requirements.txt: Lists all the required libraries for the project (e.g., OpenCV, Tesseract, TensorFlow, Keras). This file ensures you can install all dependencies using pip install -r requirements.txt.
    README.md: A file that explains how to set up and run the project, including the installation of dependencies, how to capture images, and how to classify products.
