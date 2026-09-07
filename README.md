# ED Material Tracker

Standalone Elite Dangerous engineering material monitor with a dark E:D-orange GUI.

## Features

- Polls journal files every 5 minutes
- Tracks all Raw, Encoded, and Manufactured engineering materials
- Dark theme with E:D orange accents
- Visual quantity bars
- Directory picker on first launch
- Portable — no installation required

## Usage

### Run from Python
```
python ed_material_tracker.py
```

### Build Windows executable
```
build.bat
```
Then run `dist/ED_Material_Tracker.exe` — standalone, no Python needed on target machine.

## How it works

1. On launch, asks you to select your Elite Dangerous journal directory
2. Parses the most recent `Materials` event from journal logs
3. Displays all materials grouped by category (Raw/Encoded/Manufactured)
4. Auto-refreshes every 5 minutes

## Requirements

- Python 3.10+ (for running from source)
- Elite Dangerous journal files (the game generates these automatically)
