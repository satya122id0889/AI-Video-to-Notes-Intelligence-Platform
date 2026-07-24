# 🎥 YouTube Lecture Keyframe Extractor

Automatically convert YouTube lecture videos into concise, printable notes by extracting the most informative slides using **OCR**, **BERT embeddings**, and **semantic change detection**.

Instead of saving hundreds of screenshots, this project intelligently identifies slide transitions, selects representative keyframes, and allows users to export the final selection as a PDF.

---

## ✨ Features

- 📥 Download YouTube videos directly using **yt-dlp**
- 🎞️ Extract screenshots at fixed time intervals
- 🔍 Perform OCR using **EasyOCR**
- 🧹 Clean OCR text for improved semantic analysis
- 🧠 Generate semantic embeddings with **BERT**
- 📊 Detect slide changes using cosine similarity
- 🎯 Select the most informative frame from each segment
- 🖼️ Interactive Flask web interface for reviewing keyframes
- 📄 Export selected keyframes as a PDF

---

## 📌 Motivation

Lecture videos often contain hundreds of nearly identical frames. Manually selecting important slides is time-consuming and inefficient.

This project automates the process by analyzing the **semantic content** of each frame rather than relying solely on pixel-level differences, making it suitable for educational videos, online courses, presentations, and recorded lectures.

---

## 🏗️ Pipeline

```text
YouTube Video
      │
      ▼
Download (yt-dlp)
      │
      ▼
Frame Extraction
(0.5 sec interval)
      │
      ▼
OCR (EasyOCR)
      │
      ▼
Text Cleaning
      │
      ▼
BERT Embeddings
      │
      ▼
Cosine Similarity
      │
      ▼
Slide Change Detection
      │
      ▼
Representative Frame Selection
      │
      ▼
Flask Interface
      │
      ▼
User Selection
      │
      ▼
PDF Generation
```

---

## 📂 Project Structure

```text
.
├── app.py
├── templates/
│   └── index.html
├── yt_csv/
│   ├── screenshots.csv
│   ├── screenshots_with_ocr.csv
│   ├── screenshots_with_cleaned_text.csv
│   └── keyframes_by_segment_nonempty.csv
├── yt_screenshots/
│   ├── frame_00001.jpg
│   ├── frame_00002.jpg
│   └── ...
├── models/
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Backend | Flask |
| Video Download | yt-dlp |
| Video Processing | OpenCV |
| OCR | EasyOCR |
| NLP | Hugging Face Transformers (BERT) |
| Machine Learning | PyTorch |
| Data Processing | Pandas, NumPy |
| Similarity | Scikit-learn |
| Image Processing | Pillow |

---

## 🚀 How It Works

### 1. Download Video

The application downloads a YouTube video using **yt-dlp** while preserving the highest available quality.

### 2. Extract Frames

Frames are captured every **0.5 seconds** using OpenCV.

Example:

```text
frame_00001.jpg
frame_00002.jpg
frame_00003.jpg
...
```

### 3. OCR Extraction

Each frame is processed using **EasyOCR** to extract visible text.

Example:

```text
BIOLO6Y SMALL INTESTINE Food AbsorptiOn
```

↓

```text
small intestine food absorption
```

### 4. Text Cleaning

The extracted OCR text is cleaned by:

- Converting to lowercase
- Removing punctuation
- Filtering noisy OCR tokens
- Preserving meaningful words

### 5. Semantic Embedding

Every cleaned text is converted into a **768-dimensional BERT embedding**, enabling semantic comparison between frames.

### 6. Change Detection

Cosine similarity is computed between consecutive embeddings.

When similarity falls below a predefined threshold, a new lecture segment is detected.

### 7. Representative Keyframe Selection

For every detected segment:

- Compute OCR text length
- Identify the frame with the richest textual content
- Skip segments without useful text

### 8. Interactive Review

The selected keyframes are displayed in a Flask web application.

Users can:

- Review extracted slides
- Deselect unwanted frames
- Generate a PDF containing only the selected slides

---

## 📈 Example

**Input**

- Video Duration: ~3.5 minutes
- Frames Extracted: **418**

⬇️

**Automatic Processing**

- OCR
- BERT Embeddings
- Semantic Segmentation

⬇️

**Output**

- Representative Keyframes: **30**
- Ready-to-download PDF

---

## 💡 Future Improvements

- Replace BERT with **Sentence-BERT** for faster inference
- Combine OCR embeddings with **CLIP** image embeddings
- Automatic slide summarization using an LLM
- Adaptive similarity thresholds
- Batch processing of multiple videos
- Transcript-aware slide selection
- Searchable PDF generation

---

## 🎯 Applications

- 📚 Lecture note generation
- 🎓 Educational video summarization
- 📝 Online course revision
- 📊 Presentation slide extraction
- 🎥 Meeting recording summarization
- 📄 Study material creation

---

## 🤝 Contributing

Contributions are welcome!

Feel free to open an issue or submit a pull request if you have ideas for improving the OCR pipeline, semantic segmentation, or user interface.

---


## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
