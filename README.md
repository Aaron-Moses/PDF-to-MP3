```markdown
# PDF to Audiobook Converter

This project is a simple Flask web application that allows users to upload a PDF file, convert the text to speech, and download the resulting audiobook as an MP3 file.

## Features

- Upload a PDF file
- Extract text from the PDF
- Convert the extracted text to speech
- Download the audiobook in MP3 format

## Technologies Used

- Flask: Web framework for Python
- PyPDF2: Library for PDF text extraction
- gTTS: Google Text-to-Speech library

## Project Structure

```
pdf_to_audiobook/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── uploaded_files/
└── requirements.txt
```

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/pdf-to-audiobook.git
   cd pdf_to_audiobook
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:
   ```bash
   python app.py
   ```

5. **Open your web browser and navigate to** `http://127.0.0.1:5000/` **to use the application.**
```

This README provides a concise overview of the project, its features, the technologies used, and the steps to set up and run the application.
