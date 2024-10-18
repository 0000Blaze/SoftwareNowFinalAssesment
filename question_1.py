import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

# Base class for the application
class AppBase:
    def __init__(self, master):
        self.master = master
        self.master.title("AI Image Classifier")

# Derived class for a specific AI feature
class ImageClassifier(AppBase):
    def __init__(self, master):
        super().__init__(master)  # Using inheritance
        self.model = self.load_model_image()  # Load the AI model
        self.create_widgets()  # UI elements

    def load_model_image(self):
        # Load pre-trained MobileNetV2 model with ImageNet weights
        return tf.keras.applications.MobileNetV2(weights="imagenet")

    def create_widgets(self):
        # Create UI components like buttons and labels
        self.label = tk.Label(self.master, text="Upload Image")
        self.label.pack()
        self.upload_button = tk.Button(self.master, text="Upload", command=self.upload_image)
        self.upload_button.pack()

        # Label to display the image
        self.image_label = tk.Label(self.master)
        self.image_label.pack()
    
    def upload_image(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(
            title="Choose an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )

        if file_path:
            # Load the image using Pillow and resize it for display
            image = Image.open(file_path)
            image = image.resize((250, 250))
            img = ImageTk.PhotoImage(image)

            # Display the image on the label
            self.image_label.config(image=img)
            self.image_label.image = img  # Prevent the image from being garbage collected

            # Analyze and classify the uploaded image
            self.classify_image(file_path)
        else:
            messagebox.showerror("Error", "No image was selected.")

    def preprocess_image(self, file_path):
        # Load the image and resize it to the input size of the model (224x224 for MobileNetV2)
        image = Image.open(file_path)
        image = image.resize((224, 224))
        image = np.array(image)  # Convert to numpy array
        image = tf.keras.applications.mobilenet_v2.preprocess_input(image)  # Preprocess for the model
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        return image

    def classify_image(self, file_path):
        # Preprocess the image
        processed_image = self.preprocess_image(file_path)

        # Get predictions
        predictions = self.model.predict(processed_image)

        # Decode the prediction using ImageNet labels
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0]

        # Get the highest probable class and display it
        class_name = decoded_predictions[0][1]  # Class name
        confidence = decoded_predictions[0][2]  # Confidence score

        # Show the classification result
        messagebox.showinfo("Classification Result", f"Predicted: {class_name}\nConfidence: {confidence:.2f}")

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageClassifier(root)
    root.mainloop()
