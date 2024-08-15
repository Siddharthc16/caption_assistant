import streamlit as st
from PIL import Image
import openai
import os
import uuid
from helper import CaptionHelper

# Function to save the uploaded image to a folder
def save_image(uploaded_file):
    folder_path = "uploaded_images"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    image_id = str(uuid.uuid4())
    image_path = os.path.join(folder_path, f"{image_id}.jpg")
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return image_path

# Function to delete the image after processing
def delete_image(image_path):
    if os.path.exists(image_path):
        os.remove(image_path)

# Placeholder function to simulate caption generation (replace with actual OpenAI API call)


# Streamlit UI
st.title("Social Media Caption Generator")

st.write("Upload your picture and provide some memories or context. Get 2-3 perfect captions for your social media post!")

# File upload
uploaded_file = st.file_uploader("Choose a picture...", type=["jpg", "jpeg", "png"])
memories = st.text_area("Memories or context (optional)", placeholder="Share any memories or thoughts related to the picture...")

if uploaded_file is not None:
    # Save the uploaded image
    image_path = save_image(uploaded_file)
    image = Image.open(image_path)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Generate Captions"):
        # Generate captions
        helper = CaptionHelper()
        captions = helper.generate_captions(image_path, memories)
        
        
        # Display captions
        st.write("### Generated Captions:")
        
        st.write(f"{captions}")
        
        # Delete the image after processing
        delete_image(image_path)
