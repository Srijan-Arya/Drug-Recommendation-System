# 💊 Drug Recommendation System 

Welcome to the **Drug Recommendation System**! This project aims to provide an intelligent solution for recommending similar drugs based on user input. It utilizes Natural Language Processing (NLP) and machine learning to offer efficient and accurate drug recommendations.

![image](https://github.com/user-attachments/assets/65c92b39-fc72-4500-ad39-3f7e38f3b269)


## 🛠️ Project Overview

This application leverages TF-IDF Vectorization and cosine similarity to analyze drug names and recommend similar options. Built using Python and Streamlit, it offers an interactive and user-friendly interface for drug recommendations.

## 📦 Features

- **Drug Recommendations**: Suggests similar drugs based on user input.
- **User-Friendly Interface**: Built with Streamlit for a clean and interactive experience.
- **Efficient Data Handling**: Uses compressed `.joblib` files to optimize performance.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `pip` for package management

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Srijan-Arya/Drug-Recommendation-System.git
   cd Drug-Recommendation-System
   ```
   
2. **Create a Virtual Environment**
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   
4. **bashInstall Dependencies***
   ```bash
   pip install -r requirements.txt
   ```
   
5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## 💻 How It Works

The **Drug Recommendation System** employs a combination of Natural Language Processing (NLP) and machine learning techniques to recommend similar drugs based on user input. Here’s a step-by-step breakdown of the process:

### 1. **Data Processing**

- **Loading Data**: The system starts by loading the dataset containing drug names and related information from `medicine.csv`.

- **Preprocessing**:
  - **Normalization**: Drug names are converted to lowercase to ensure uniformity.
  - **Cleaning**: Special characters and unnecessary symbols are removed from drug names using regular expressions. This helps in standardizing the data for further processing.

### 2. **Feature Extraction**

- **TF-IDF Vectorization**:
  - **Term Frequency-Inverse Document Frequency (TF-IDF)** is used to convert text data into numerical features.
  - **TF-IDF Vectorizer** calculates how important a word is to a document in a collection, adjusting for the frequency of the word in other documents.
  - The vectorizer creates a matrix where each row represents a drug, and each column represents a unique term from the dataset, weighted by its importance.

### 3. **Similarity Calculation**

- **Cosine Similarity**:
  - **Cosine Similarity** is used to measure the similarity between the TF-IDF vectors of different drugs.
  - The similarity score ranges from 0 (no similarity) to 1 (identical). This metric helps in finding how closely related two drugs are based on their names.

- **Computing the Similarity Matrix**:
  - The similarity matrix is a square matrix where each entry (i, j) represents the cosine similarity between the i-th and j-th drug.
  - This matrix is saved as a compressed `.joblib` file for efficient storage and retrieval.

### 4. **Recommendation System**

- **Recommendation Function**:
  - **Finding the Index**: The function takes a user’s input (a drug name), finds its index in the dataset, and retrieves its similarity scores.
  - **Sorting and Filtering**: The function sorts the drugs based on similarity scores, excluding the drug itself, and selects the top recommendations.
  - **Output**: The names of the recommended drugs are returned to the user.

### 5. **Streamlit Application**

- **User Interface**:
  - The Streamlit app provides an interactive interface where users can select a drug from a dropdown menu.
  - Upon selection, the app uses the recommendation function to generate and display similar drugs.

- **Image and Styling**:
  - Custom styling and images are used to enhance the visual appeal of the app.

### 6. **Deployment**

- **GitHub and Streamlit**:
  - The code, along with the compressed `.joblib` files, is hosted on GitHub.
  - Streamlit is used to deploy the application, making it accessible through a web browser.

## 🛠️ Technical Details

- **Libraries and Tools**:
  - **Python**: The programming language used for the implementation.
  - **scikit-learn**: Provides tools for TF-IDF Vectorization and cosine similarity computation.
  - **joblib**: Used for compressing and saving the large similarity matrix efficiently.
  - **Streamlit**: Framework for building and deploying the interactive web application.

