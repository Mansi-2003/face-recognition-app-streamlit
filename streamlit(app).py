from PIL import Image
import numpy as np


import streamlit as st
#title
st.title("Face Recognition App")

#Sub header
st.subheader("Face Recognition Model Deployment")

#To give information
st.info(
    "This application uses a pre-trained face recognition model to detect and recognize faces in images or real-time video. "
    "You can upload an image or use your webcam to test the recognition capabilities."
)

#Write
st.write("Welcome to the Face Recognition App. Please upload an image or use your webcam to begin.")

uploaded_image = st.file_uploader("Upload a face image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Load the uploaded image
    image = Image.open(uploaded_image)
    image_np = np.array(image)

    # Find all face locations
    face_locations = face_recognition.face_locations(image_np)

    # Display result
    if face_locations:
        st.success(f"Detected {len(face_locations)} face(s) in the uploaded image.")
    else:
        st.warning("No faces were detected in the image.")

    # Webcam input
camera_image = st.camera_input("Take a picture")

if camera_image is not None:
    # Convert to numpy array
    image = Image.open(camera_image)
    image_np = np.array(image)

    # Detect faces
    face_locations = face_recognition.face_locations(image_np)

    if face_locations:
        st.success(f"Detected {len(face_locations)} face(s) in the webcam image.")
    else:
        st.warning("No face detected in webcam image.")



