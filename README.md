# SoundPad

A simple, scalable web-based soundpad built with Python Flask.

## Features

- **Easy Sound Adding**: Just drop audio files in the `sounds` folder and refresh!
- **Scalable**: Automatically detects and displays all audio files
- **Loop Control**: Check the "Loop" checkbox to repeat any sound continuously
- **Individual Sound Control**: Stop specific sounds or all sounds at once
- **Visual Feedback**: See which sounds are currently playing with highlighted cards
- **Now Playing Display**: Real-time list of all active sounds with individual stop buttons
- **Easy to Use**: Click buttons to play sounds, keyboard shortcuts (1-9, 0)
- **Web-based**: Works in any browser
- **Multiple Format Support**: MP3, WAV, OGG, M4A, FLAC

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Your Sounds

Add audio files (.mp3, .wav, etc.) to the `sounds` folder.

The filename will become the button name:
- `laugh.mp3` -> Button labeled "laugh"
- `airhorn.wav` -> Button labeled "airhorn"

### 3. Run the Server

```bash
python app.py
```

### 4. Open in Browser

Go to: `http://127.0.0.1:5000`

## How to Use

1. **Play a sound**: Click any sound button
2. **Loop a sound**: Check the "Loop" checkbox before or after clicking to repeat continuously
3. **Stop individual sound**: Click the "Stop" button next to the sound in the "Now Playing" section
4. **Stop all sounds**: Click "Stop All Sounds" button at the top
5. **See what's playing**: Check the "Now Playing" section - highlighted cards also show active sounds
6. **Add new sounds**: Drop files in `sounds` folder and click "Refresh Sounds"
7. **Keyboard shortcuts**: Press 1-9 or 0 to play the first 10 sounds

## Hosting on GitHub

1. Create a new repository on GitHub
2. Push this code:


## Adding More Sounds

Just drop more audio files into the `sounds` folder at any time. Refresh the page to see them!

No code changes needed!

## Project Structure

```
SoundPad/
├── app.py                  # Main Flask server
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Web interface
└── sounds/                # Put your audio files here!
    └── ADD_SOUNDS_HERE.txt
```

## Notes

- Appearance is minimal/functional by design
- Extremely easy to add new sounds (no config files!)
- Scales to hundreds of sounds automatically
- Works on any device with a web browser
