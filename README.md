Image Similarity Finder ✨
This project is a web application that allows users to find images similar to a given query image from a gallery of uploaded images. It leverages a pre-trained ResNet50 model for feature extraction and cosine similarity for comparison.
Table of Contents
Features
How It Works
Demo
Setup
Usage
Project Structure
Features 🚀
Upload Query Image: Upload a single image to use as the basis for similarity search.
Upload Gallery Images: Upload multiple images to create a gallery against which the query image will be compared.
Image Feature Extraction: Utilizes a pre-trained ResNet50 model (without its final classification layer) to extract robust features from images.
Cosine Similarity: Compares the feature vectors of the query image and gallery images using cosine similarity to determine their resemblance.
Top Matches Display: Shows the top 5 most similar images from the gallery along with their similarity scores.
Download Matches: Provides an option to download the top-matched images as a ZIP archive.
Reset Functionality: Clears all uploaded images and results.
How It Works 🧠
The core of this application lies in its ability to understand and compare images based on their visual content.
Feature Extraction (utils.py):
A pre-trained ResNet50 model from torchvision.models is loaded. This model has been trained on a vast dataset (ImageNet) and is excellent at recognizing general features in images.
The final classification layer of the ResNet50 model is removed, allowing us to extract the high-level features learned by the network rather than its classification predictions.
Input images are resized, converted to tensors, and normalized to match the expected input format of the ResNet model.
For each image (query and gallery), its feature vector is extracted using the modified ResNet50 model. These feature vectors are essentially numerical representations of the image's content.
Gallery Indexing (utils.py):
All images uploaded to the gallery are processed, and their feature vectors are extracted and stored.
Similarity Calculation (utils.py):
When a query image is submitted, its feature vector is compared against all feature vectors in the gallery using cosine_similarity from sklearn.metrics.pairwise. Cosine similarity measures the cosine of the angle between two non-zero vectors, indicating how similar their directions are. A higher cosine similarity (closer to 1) means the images are more similar.
Web Interface (app.py, index.html, style.css):
A Flask web application handles image uploads, processes the similarity search by calling functions from utils.py, and renders the results using an HTML template.
The index.html provides the user interface for uploading images and displaying results.
The style.css provides the styling for the web application.
![Screenshot of the application](<img width="1917" height="935" alt="Screenshot 2025-07-22 020104" src="https://github.com/user-attachments/assets/8bb62aa2-42ff-46af-9c24-50818f87729f" />
)
Setup ⚙️
To set up and run this project locally, follow these steps:
Prerequisites
Python 3.x
pip (Python package installer)
Installation
Clone the repository:
git clone <your-repository-url>
cd image-similarity-finder


Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install Flask torch torchvision scikit-learn numpy Pillow


Usage ▶️
Run the Flask application:
python app.py

The application will typically run on http://127.0.0.1:5000/.
Open in your browser:
Navigate to http://127.0.0.1:5000/ in your web browser.
Upload Images:
Upload a single query image: Choose the image you want to find similar matches for.
Upload gallery images: Select multiple images that will form your search gallery.
Find Similar Images:
Click the "Find Similar Images" button. The application will process the images and display the top matches.
Download Matches:
If results are displayed, click the "Download Matches as ZIP" button to download a ZIP archive containing the top similar images.
Reset:
Click the "Reset" button to clear all uploaded images and start a new search.
Project Structure 📁
.
├── app.py              # Flask application logic
├── utils.py            # Image feature extraction and similarity calculation
├── static/
│   ├── style.css       # Styling for the web application
│   ├── uploaded_gallery/ # Directory for uploaded gallery images (created by app.py)
│   └── uploaded_query/   # Directory for uploaded query image (created by app.py)
└── templates/
    └── index.html      # HTML template for the web interface
├── README.md           # This file


