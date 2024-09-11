import streamlit as st
import pickle
import pandas as pd
import requests
import os
from PIL import Image


# URLs of the .pkl files (replace these with actual links from Google Drive, Dropbox, etc.)
SIMILARITY_PKL_URL = "https://drive.google.com/file/d/1Qpm7GlehsmrowQof9hEO7yT3yl8nakob/view?usp=sharing"
# MEDICINE_DICT_PKL_URL = "https://drive.google.com/uc?id=YOUR_FILE_ID_FOR_MEDICINE_DICT"

# Function to download .pkl files
def download_file(url, file_path):
    if not os.path.exists(file_path):
        st.write(f"Downloading {file_path}...")
        response = requests.get(url)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        st.write(f"{file_path} downloaded successfully!")

# Ensure files are available locally
download_file(SIMILARITY_PKL_URL, "similarity.pkl")
# download_file(MEDICINE_DICT_PKL_URL, "medicine_dict.pkl")

# Load the .pkl files after ensuring they are downloaded
medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(medicine):
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
    return recommended_medicines

# Title of the Application
st.markdown("<h1 style='text-align: center; color: #007bff;'>Drug Recommendation System</h1>", unsafe_allow_html=True)

# Image (center the image and set custom width)
image = Image.open('images/medss.png')

# Create empty columns to center the image
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(image, caption='', width=350)  # Set width to 350px

# Searchbox and recommendation
st.markdown("<h3 style='color: #2c3e50;'>Find Similar Drugs:</h3>", unsafe_allow_html=True)

# Organize layout with columns for better visual separation
col1, col2 = st.columns([3, 1])

with col1:
    selected_medicine_name = st.selectbox('Select a medicine to get similar recommendations:', medicines['Drug_Name'].values)

with col2:
    # Add a button with a customized style
    st.markdown("""
    <style>
        .stButton button {
            margin-top: 8px;
            background-color: #28a745;
            color: white;
            border-radius: 10px;
            padding: 0.5em;
            width: 100%;
            height: 100%;
        }
    </style>""", unsafe_allow_html=True)
    recommend_btn = st.button('Recommend Drug')

# Display recommendations if the button is pressed
if recommend_btn:
    recommendations = recommend(selected_medicine_name)
    
    st.markdown("<h3 style='color: #34495e;'>Recommended Drugs:</h3>", unsafe_allow_html=True)
    
    # Create a new column layout for recommendations to use full width
    for idx, drug in enumerate(recommendations, start=1):
        st.markdown(f"""
        <style>
            .recommendation-link {{
                color: lightgrey;
                text-decoration: none;
            }}
            .recommendation-link:hover {{
                color: #007bff;
                text-decoration: underline;
            }}
        </style>
        <p style='font-size:18px; border:4px solid #34495e; padding: 10px; border-radius:20px;'>
            <a href='https://pharmeasy.in/search/all?name={drug}' class='recommendation-link'>{drug}</a>
        </p>""", unsafe_allow_html=True)

# Footer for credits or additional information
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7f8c8d;'>Made by <span style='color: orange'>Srijan Arya </span> | <a href='https://github.com/' style='text-decoration:none'>Github</a> © 2024</p>", unsafe_allow_html=True)
