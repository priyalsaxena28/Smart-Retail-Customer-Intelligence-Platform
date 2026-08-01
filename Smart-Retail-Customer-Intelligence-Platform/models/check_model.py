from tensorflow.keras.models import load_model

model = load_model("models/product_classifier.h5")

print("Output Shape:", model.output_shape)
print("Number of Classes:", model.output_shape[-1])