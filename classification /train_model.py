from tensorflow.keras.preprocessing.image import ImageDataGenerator
from cnn_model import build_cnn_model

# Data preparation
train_datagen = ImageDataGenerator(rescale=1./255)
train_data = train_datagen.flow_from_directory(
    '../data/training_data/',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary'
)

# Build and compile the CNN model
cnn_model = build_cnn_model()

# Train the model
cnn_model.fit(train_data, epochs=10, steps_per_epoch=100)

# Save the trained model
cnn_model.save('../output/cnn_model.h5')
