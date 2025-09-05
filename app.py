from flask import Flask, request, render_template, url_for, jsonify
import pyttsx3
import os
from transformers import pipeline

app = Flask(__name__)

# Ensure static folder exists
os.makedirs('static', exist_ok=True)
AUDIO_FILE = "static/output.wav"

# Initialize TTS engine
engine = pyttsx3.init()

# Hugging Face emotion classifier
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

# Base vocal parameters for each emotion
emotion_params = {
    "joy": {"rate": 180, "volume": 1.0},
    "sadness": {"rate": 120, "volume": 0.8},
    "anger": {"rate": 110, "volume": 0.7},
    "fear": {"rate": 130, "volume": 0.8},
    "surprise": {"rate": 190, "volume": 1.0},
    "neutral": {"rate": 150, "volume": 0.9},
}

# Detect emotion + intensity
def detect_emotion(text):
    results = emotion_classifier(text)[0]
    # pick label with highest score
    best = max(results, key=lambda x: x['score'])
    return best['label'].lower(), best['score']

# Generate speech with intensity scaling
def generate_speech(text, emotion, intensity):
    params = emotion_params.get(emotion, emotion_params['neutral'])
    rate = params['rate'] + int(params['rate'] * intensity * 0.5)
    volume = min(params['volume'] + intensity * 0.5, 1.0)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    engine.save_to_file(text, AUDIO_FILE)
    engine.runAndWait()
    return AUDIO_FILE

@app.route('/detect', methods=['POST'])
def detect():
    text = request.json.get('text', '')
    if not text.strip():
        return jsonify({"emotion": None, "intensity": None})
    emotion, intensity = detect_emotion(text)
    return jsonify({"emotion": emotion.capitalize(), "intensity": round(intensity, 2)})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form.get('text')
    if not text.strip():
        return render_template('index.html', audio=None, emotion=None, intensity=None)

    emotion, intensity = detect_emotion(text)
    audio_path = generate_speech(text, emotion, intensity)
    return render_template('index.html',
                           audio=url_for('static', filename='output.wav'),
                           emotion=emotion.capitalize(),
                           intensity=round(intensity, 2))

if __name__ == "__main__":
    app.run(debug=True)
