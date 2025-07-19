# 🐱 Cute Cat Alarm Clock

A beautiful and functional alarm clock GUI application built with Python that features:

- 🎨 Cute cat background image (automatically downloaded)
- ⏰ Digital time and date display
- 🔔 Easy alarm setting with hour/minute spinboxes
- 🎵 Custom "Jaago jaago subh ho gyi" inspired alarm melody
- 🛑 Alarm control buttons (Set, Cancel, Test, Stop)
- 🎪 Attractive and user-friendly interface

## Features

- **Beautiful GUI**: Features a cute cat background with an elegant overlay
- **Real-time Clock**: Shows current time and date with automatic updates
- **Alarm Functionality**: Set alarms with hour and minute precision
- **Custom Sound**: Plays a cheerful melody inspired by "Jaago jaago subh ho gyi"
- **Test Feature**: Test your alarm sound before setting it
- **Visual Feedback**: Color-coded status messages and button states
- **Modal Alarm**: Attention-grabbing alarm window when the alarm rings

## Installation

### Prerequisites
- Python 3.7 or higher
- Internet connection (for downloading cat background image)

### Setup

1. **Clone or download** this project to your local machine

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv alarm_venv
   source alarm_venv/bin/activate  # On Windows: alarm_venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate the alarm sound** (optional - automatically done when running the app):
   ```bash
   python create_alarm_sound.py
   ```

## Usage

1. **Run the alarm clock**:
   ```bash
   source alarm_venv/bin/activate  # Activate virtual environment
   python alarm_clock.py
   ```

2. **Set an alarm**:
   - Use the hour and minute spinboxes to select your desired alarm time
   - Click the "🔔 Set Alarm" button
   - The status will show your alarm time

3. **Test the alarm**:
   - Click "🎵 Test Alarm" to hear the alarm sound

4. **Cancel an alarm**:
   - Click "❌ Cancel Alarm" to disable the current alarm

5. **When the alarm rings**:
   - A popup window will appear with the message "🐱 JAAGO JAAGO SUBH HO GYI! 🐱"
   - The alarm sound will play continuously
   - Click "🛑 Stop Alarm" to stop the alarm

## File Structure

```
alarm-clock/
├── alarm_clock.py          # Main application file
├── create_alarm_sound.py   # Script to generate alarm sound
├── alarm_sound.wav         # Generated alarm melody file
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Technical Details

- **GUI Framework**: Tkinter (built-in with Python)
- **Audio**: Pygame for sound playback
- **Images**: PIL/Pillow for image processing
- **Networking**: Requests for downloading background image
- **Sound Generation**: Pure Python sine wave generation

## Customization

### Change Background Image
Edit the `cat_image_url` variable in `alarm_clock.py` to use a different background image.

### Modify Alarm Sound
Edit the `melody` list in `create_alarm_sound.py` to create your own alarm tune, then run:
```bash
python create_alarm_sound.py
```

### Adjust Colors and Fonts
Modify the color codes and font specifications in the `setup_widgets()` method.

## Troubleshooting

### No Internet Connection
If you can't download the cat background, the app will use a beautiful gradient background instead.

### Sound Issues
- Make sure your system audio is working
- The app will fall back to system beep if there are audio issues
- Try running the test alarm to check sound functionality

### Display Issues
- Make sure your screen resolution is at least 800x600
- The window is automatically centered on your screen

## Requirements

- Python 3.7+
- pygame
- Pillow (PIL)
- requests
- tkinter (usually included with Python)

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to fork this project and submit improvements! Some ideas for enhancements:
- Multiple alarm support
- Snooze functionality
- Different alarm sounds
- Themes and customization options
- Volume control

---

**Wake up with style! 🐱⏰**