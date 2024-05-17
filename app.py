from flask import Flask, render_template, request, send_file
import PyPDF2
from gtts import gTTS
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploaded_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        text = extract_text_from_pdf(file_path)
        audio_path = text_to_speech(text, f'{UPLOAD_FOLDER}/output.mp3')
        return send_file(audio_path, as_attachment=True)

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_speech(text, output_path):
    tts = gTTS(text)
    tts.save(output_path)
    return output_path

if __name__ == '__main__':
    app.run(debug=True)
