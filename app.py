from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

SOUNDS_DIR = 'sounds'

def get_sound_files():
    """Automatically detect all audio files in the sounds directory"""
    if not os.path.exists(SOUNDS_DIR):
        os.makedirs(SOUNDS_DIR)
        return []

    audio_extensions = ['.mp3', '.wav', '.ogg', '.m4a', '.flac']
    sound_files = []

    for file in os.listdir(SOUNDS_DIR):
        if any(file.lower().endswith(ext) for ext in audio_extensions):
            # Use filename without extension as button name
            name = os.path.splitext(file)[0]
            sound_files.append({'name': name, 'file': file})

    return sorted(sound_files, key=lambda x: x['name'])

@app.route('/')
def index():
    sounds = get_sound_files()
    return render_template('index.html', sounds=sounds)

@app.route('/sounds/<path:filename>')
def serve_sound(filename):
    """Serve audio files"""
    return send_from_directory(SOUNDS_DIR, filename)

if __name__ == '__main__':
    # Create sounds directory if it doesn't exist
    if not os.path.exists(SOUNDS_DIR):
        os.makedirs(SOUNDS_DIR)

    print("=" * 50)
    print("SOUNDPAD SERVER STARTING")
    print("=" * 50)
    print(f"Add your sound files (.mp3, .wav, etc.) to the '{SOUNDS_DIR}' folder")
    print("Then refresh the page to see them appear!")
    print("Server running at: http://127.0.0.1:5000")
    print("=" * 50)

    app.run(debug=True, host='0.0.0.0', port=5000)
