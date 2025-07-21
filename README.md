# Image Similarity Finder ✨  

**Find visually similar images in your gallery with ease!**  

This web application helps you discover images similar to a given query image from a gallery of uploaded images. Powered by a **pre-trained ResNet50 model** for feature extraction and **cosine similarity** for comparison, it delivers accurate and fast results.  

![App Screenshot](https://github.com/user-attachments/assets/8bb62aa2-42ff-46af-9c24-50818f87729f)  

---

## Features 🚀  

✅ **Upload Query Image** – Select a single image as the basis for similarity search  
✅ **Upload Gallery Images** – Add multiple images to compare against  
✅ **Feature Extraction** – Uses ResNet50 to extract high-level image features  
✅ **Smart Matching** – Finds top 5 similar images using cosine similarity  
✅ **Download Results** – Export matches as a ZIP archive  
✅ **Reset Functionality** – Clear all uploads with one click  

---

## How It Works 🧠  

1. **Feature Extraction**  
   - Pre-trained ResNet50 processes images into numerical feature vectors  
   - Final classification layer removed to focus on visual features  

2. **Similarity Calculation**  
   - Compares query image features against gallery using cosine similarity  
   - Scores range from 0 (dissimilar) to 1 (identical)  

3. **Web Interface**  
   - Flask backend handles image processing  
   - Clean HTML/CSS frontend displays results intuitively  

---

## Installation ⚙️  

```bash
# Clone repository
git clone https://github.com/your-username/image-similarity-finder.git
cd image-similarity-finder

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install Flask torch torchvision scikit-learn numpy Pillow
