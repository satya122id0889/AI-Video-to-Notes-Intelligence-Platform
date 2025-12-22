from flask import Flask, render_template, request, send_file, redirect, url_for
import pandas as pd
import os
from PIL import Image
import io

app = Flask(__name__)

app = Flask(__name__)

@app.template_filter('hms')
def seconds_to_hms(seconds):
    seconds = int(float(seconds))
    return f"{seconds//3600:02}:{(seconds%3600)//60:02}:{seconds%60:02}"


# Path configurations
CSV_PATH = "./yt_csv/keyframes_by_segment_nonempty.csv"  # adjust if needed
IMG_FOLDER = "./yt_screenshots"

# Load CSV once at startup
df = pd.read_csv(CSV_PATH)
# Expect df has at least 'filename' and 'timestamp (seconds)'
filenames = df['filename'].tolist()
timestamps = df['timestamp (seconds)'].tolist()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get list of selected filenames from form
        selected = request.form.getlist("selected")  # values are filenames
        if not selected:
            # No images selected; redirect back with a message or just regenerate empty PDF
            return redirect(url_for('index'))
        # Generate PDF in-memory
        pdf_bytes = create_pdf_bytes(selected)
        # Send as file download
        return send_file(
            pdf_bytes,
            mimetype="application/pdf",
            as_attachment=True,
            download_name="selected_keyframes.pdf"
        )
    else:
        # GET: render all images with checkboxes checked by default
        items = list(zip(filenames, timestamps))
        return render_template("index.html", items=items)

def create_pdf_bytes(selected_filenames):
    """
    Given a list of filenames (in order), open each image and compile into a single PDF.
    Returns a BytesIO object positioned at start.
    """
    pil_images = []
    for fname in selected_filenames:
        img_path = os.path.join(IMG_FOLDER, fname)
        try:
            img = Image.open(img_path)
            # Convert to RGB if needed
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            else:
                img = img.convert("RGB")
            pil_images.append(img)
        except Exception as e:
            print(f"Warning: could not open image {img_path}: {e}")
    if not pil_images:
        # Return an empty PDF? Create a 1-page blank PDF
        blank = Image.new("RGB", (800, 600), color="white")
        bio = io.BytesIO()
        blank.save(bio, format="PDF")
        bio.seek(0)
        return bio

    # Save to BytesIO
    bio = io.BytesIO()
    first, rest = pil_images[0], pil_images[1:]
    first.save(bio, format="PDF", save_all=True, append_images=rest)
    bio.seek(0)
    return bio

@app.route("/images/<path:filename>")
def serve_image(filename):
    """
    Serve image files from IMG_FOLDER.
    """
    return send_file(os.path.join(IMG_FOLDER, filename))

if __name__ == "__main__":
    app.run(debug=True)
