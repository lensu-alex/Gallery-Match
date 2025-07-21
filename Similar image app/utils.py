import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50
from PIL import Image
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity

# Load pre-trained model (without final classification layer)
model = resnet50(pretrained=True)
model = torch.nn.Sequential(*list(model.children())[:-1])
model.eval()

# Preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

def extract_features(image_path):
    img = Image.open(image_path).convert("RGB")
    tensor = transform(img).unsqueeze(0)
    with torch.no_grad():
        feature = model(tensor).squeeze().numpy()
    return feature / np.linalg.norm(feature)

def index_gallery(gallery_path):
    features = []
    image_names = []
    for file in os.listdir(gallery_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            path = os.path.join(gallery_path, file)
            try:
                features.append(extract_features(path))
                image_names.append(file)
            except Exception as e:
                print(f"Error processing {file}: {e}")
    return np.array(features), image_names

def find_similar_images(query_image_path, gallery_folder, top_k=5):
    query_feature = extract_features(query_image_path).reshape(1, -1)
    gallery_features, image_names = index_gallery(gallery_folder)

    if len(gallery_features) == 0:
        return []

    similarities = cosine_similarity(query_feature, gallery_features)[0]
    top_indices = np.argsort(similarities)[::-1][:top_k]

    return [(os.path.join('uploaded_gallery/', image_names[i]), similarities[i]) for i in top_indices]
