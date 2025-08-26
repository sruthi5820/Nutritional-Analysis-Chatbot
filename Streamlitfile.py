# 
import streamlit as st
import base64
import cv2
import numpy as np
import pytesseract
import google.generativeai as genai
from io import BytesIO

# Configure Gemini AI
genai.configure(api_key="AIzaSyCPqe69b1KpksGmv3Pa9EWmEDlqXMK72Ds")

# Function to perform OCR
def perform_ocr(image):
    """Perform OCR on an uploaded image and return extracted text."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(threshold)
    return text

# Function to extract text using Gemini AI
def extract_text_with_gemini(text):
    """Extract structured information using Gemini AI."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        Please extract and analyze the nutritional information and ingredients from the following text.
        Provide a structured output with the following:
        1. List of ingredients
        2. Nutritional facts (calories, fats, carbs, proteins)
        3. Any health claims mentioned
        4. Potential allergens

        Text:
        {text}
        """
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        return f"Error with Gemini extraction: {str(e)}"

# Function to perform health analysis with Gemini AI
def health_analysis(product_info, user_profile):
    """Generate a health analysis of the product using Gemini AI, personalized for the user."""
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        name = user_profile.get('name', 'User')
        age = user_profile.get('age', 'Unknown')
        height = user_profile.get('height', 'Unknown')
        weight = user_profile.get('weight', 'Unknown')
        medical_conditions = user_profile.get('medical_conditions', 'None')

        prompt = f"""
        Generate a health analysis for the following product information considering the user's profile:

        User Profile:
        Name: {name}
        Age: {age}
        Height: {height}
        Weight: {weight}
        Medical Conditions: {medical_conditions}

        Product Information: {product_info}

        Analysis:
        """
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        return f"Error generating health analysis: {str(e)}"

# Function to answer questions based on extracted context
def answer_question_with_gemini(context, question, user_profile):
    """Use Gemini AI to answer a question based on the extracted and stored context."""
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        prompt = f"""
        Based on the following context about a food product and user profile, please answer the question.

        Context:
        {context}

        User Profile:
        Name: {user_profile['name']}
        Age: {user_profile['age']}
        Height: {user_profile['height']}
        Weight: {user_profile['weight']}
        Medical Conditions: {', '.join(user_profile['medical_conditions'])}

        Question: {question}

        Answer:
        """
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        return f"Error with Gemini Q&A: {str(e)}"

# Streamlit app layout
def main():
    st.title("Nutrition Assistant Chatbot")
    st.write("Upload an image of the food label to get nutritional analysis.")

    # User profile collection
    user_profile = {}
    user_profile['name'] = st.text_input("Name")
    user_profile['age'] = st.text_input("Age")
    user_profile['height'] = st.text_input("Height (e.g., 5'10\")")
    user_profile['weight'] = st.text_input("Weight (e.g., 70 kg)")
    conditions = st.text_input("Medical conditions (comma-separated)")
    user_profile['medical_conditions'] = [cond.strip() for cond in conditions.split(',')] if conditions else []

    # Image upload
    uploaded_file = st.file_uploader("Choose a food label image", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        # Convert the uploaded file to an OpenCV format
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Perform OCR
        ocr_text = perform_ocr(image)
        
        # Extract structured text with Gemini
        extracted_info = extract_text_with_gemini(ocr_text)

        # Generate health analysis based on user profile
        analysis = health_analysis(extracted_info, user_profile)
        st.write("Personalized Health Analysis:")
        st.write(analysis)

    # Question-answering chatbot section
    st.write("Ask questions about the product below:")
    question = st.text_input("Enter your question:")
    if st.button("Get Answer"):
        if uploaded_file is None:
            st.write("Please upload an image first.")
        else:
            answer = answer_question_with_gemini(extracted_info, question, user_profile)
            st.write("Answer:")
            st.write(answer)

if __name__ == "__main__":
    main()
