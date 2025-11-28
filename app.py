from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

SOUNDS_DIR = 'sounds'

def get_sound_files():
    """Automatically detect all audio files in the sounds directory, organized by folders"""
    if not os.path.exists(SOUNDS_DIR):
        os.makedirs(SOUNDS_DIR)
        return {}

    audio_extensions = ['.mp3', '.wav', '.ogg', '.m4a', '.flac']
    sound_groups = {}

    # Walk through all subdirectories
    for root, dirs, files in os.walk(SOUNDS_DIR):
        for file in files:
            if any(file.lower().endswith(ext) for ext in audio_extensions):
                # Get relative path from sounds directory
                rel_path = os.path.relpath(root, SOUNDS_DIR)

                # Determine group name
                if rel_path == '.':
                    group_name = 'Ungrouped'
                else:
                    # Use folder name as group, handle nested folders
                    group_name = rel_path.replace('\\', '/').split('/')[0]

                # Create group if it doesn't exist
                if group_name not in sound_groups:
                    sound_groups[group_name] = []

                # Use filename without extension as button name
                name = os.path.splitext(file)[0]
                # Store relative path from sounds directory
                file_path = os.path.relpath(os.path.join(root, file), SOUNDS_DIR).replace('\\', '/')

                sound_groups[group_name].append({
                    'name': name,
                    'file': file_path
                })

    # Sort sounds within each group
    for group in sound_groups:
        sound_groups[group] = sorted(sound_groups[group], key=lambda x: x['name'])

    # Sort groups alphabetically, but keep 'Ungrouped' last
    sorted_groups = {}
    for key in sorted(sound_groups.keys()):
        if key != 'Ungrouped':
            sorted_groups[key] = sound_groups[key]
    if 'Ungrouped' in sound_groups:
        sorted_groups['Ungrouped'] = sound_groups['Ungrouped']

    return sorted_groups

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
