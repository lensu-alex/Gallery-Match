from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from utils import find_similar_images
import os
from flask import send_file
import zipfile
import io

app = Flask(__name__)

# Folders
QUERY_FOLDER = 'static/uploaded_query'
GALLERY_FOLDER = 'static/uploaded_gallery'
os.makedirs(QUERY_FOLDER, exist_ok=True)
os.makedirs(GALLERY_FOLDER, exist_ok=True)

# Clean folders on start
for folder in [QUERY_FOLDER, GALLERY_FOLDER]:
    for f in os.listdir(folder):
        os.remove(os.path.join(folder, f))

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    query_image = None

    if request.method == 'POST':
        # Clear gallery folder
        for f in os.listdir(GALLERY_FOLDER):
            os.remove(os.path.join(GALLERY_FOLDER, f))

        # Save query image
        uploaded_query = request.files.get('query_image')
        if uploaded_query and uploaded_query.filename != '':
            filename = secure_filename(uploaded_query.filename)
            query_path = os.path.join(QUERY_FOLDER, filename)
            uploaded_query.save(query_path)
            query_image = f"uploaded_query/{filename}"

        # Save gallery images
        gallery_files = request.files.getlist('gallery_images')
        for file in gallery_files:
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(GALLERY_FOLDER, filename))

        # Run similarity search
        if query_image:
            full_query_path = os.path.join("static", query_image)
            results = find_similar_images(full_query_path, GALLERY_FOLDER)

    return render_template("index.html", results=results, query_image=query_image)

@app.route('/download_matches')
def download_matches():
    # Collect the top-matched images from the last result
    matched_images = request.args.getlist("files")

    # Create in-memory ZIP
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for file_rel_path in matched_images:
            file_path = os.path.join('static', file_rel_path)
            zip_file.write(file_path, arcname=os.path.basename(file_path))
    zip_buffer.seek(0)

    return send_file(zip_buffer, mimetype='application/zip',
                     download_name='top_matches.zip', as_attachment=True)

@app.route('/reset', methods=['POST'])
def reset():
    for folder in [QUERY_FOLDER, GALLERY_FOLDER]:
        for f in os.listdir(folder):
            os.remove(os.path.join(folder, f))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
