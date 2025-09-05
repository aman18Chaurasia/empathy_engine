# Empathy Engine 🎤

## Project Overview

The **Empathy Engine** is an AI-powered Text-to-Speech (TTS) system that transforms written text into **emotionally expressive audio**, bridging the gap between text-based sentiment and human-like voice.

It detects **emotions** from input text, modulates vocal parameters like **rate** and **volume**, and generates a playable `.wav` audio output. The web interface provides **real-time emotion feedback** as you type, making it interactive and demo-ready.

---

## Features

* **Granular emotion detection**: joy, sadness, anger, fear, surprise, anxious, neutral.
* **Intensity-based modulation**: the confidence of emotion affects speech rate and volume.
* **Live UI preview**: dynamic background and detected emotion/intensity updates as you type.
* **Flask Web App**: simple, responsive, and hackathon-ready interface.
* **Demo audio clips**: optional pre-generated clips in `static/demos/`.

---

## Tech Stack

* **Python 3**
* **Flask** for web interface
* **PyTorch + Transformers** for emotion detection
* **pyttsx3** for local TTS synthesis
* **HTML/CSS/JS** for frontend

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPO_URL>
cd empathy_engine
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux / MacOS
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### 4. Run the Flask app

```bash
python app.py
```

Open your browser at:

```
http://127.0.0.1:5000
```

---

## Usage

1. Enter your text in the textarea.
2. Observe **live emotion detection** and **dynamic background** changes.
3. Click **Generate Speech** to create a `.wav` audio file.
4. Optional: Check `static/demos/` for pre-generated audio clips.

---

## Design Choices

### Emotion-to-Voice Mapping

* **Rate and volume** are dynamically adjusted based on detected emotion and intensity:

```python
emotion_params = {
    "joy": {"rate": 180, "volume": 1.0},
    "sadness": {"rate": 120, "volume": 0.8},
    "anger": {"rate": 110, "volume": 0.7},
    "fear": {"rate": 130, "volume": 0.8},
    "surprise": {"rate": 190, "volume": 1.0},
    "anxious": {"rate": 125, "volume": 0.75},
    "neutral": {"rate": 150, "volume": 0.9},
}
```

* **Intensity scaling**: stronger emotions → faster/slower speech or higher/lower volume.

### Frontend Design

* Responsive gradient backgrounds that reflect the detected emotion.
* Real-time feedback as user types.
* Simple, intuitive interface for hackathon demos.

---

## Notes

* Works offline using `pyttsx3` for TTS.
* Requires **PyTorch** to run the Hugging Face emotion classifier.
* Optional: pre-generate demo audio clips using `demo_emotions.py`.

---

## License

MIT License
