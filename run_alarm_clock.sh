#!/bin/bash
# Simple launcher script for the Cute Cat Alarm Clock

echo "🐱 Starting Cute Cat Alarm Clock..."

# Check if virtual environment exists
if [ ! -d "alarm_venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv alarm_venv
fi

# Activate virtual environment
source alarm_venv/bin/activate

# Check if dependencies are installed
echo "Checking dependencies..."
pip install -q -r requirements.txt

# Generate alarm sound if it doesn't exist
if [ ! -f "alarm_sound.wav" ]; then
    echo "Generating alarm sound..."
    python create_alarm_sound.py
fi

# Launch the alarm clock
echo "Launching alarm clock GUI..."
python alarm_clock.py

echo "Alarm clock closed. Goodbye! 👋"