#!/usr/bin/env python3
"""
Create a pleasant alarm sound similar to "Jaago jaago subh ho gyi"
This script generates a cheerful wake-up melody.
"""

import math
import wave
import array

def generate_tone(frequency, duration, sample_rate=22050, amplitude=0.5):
    """Generate a sine wave tone"""
    frames = int(duration * sample_rate)
    tone = []
    
    for i in range(frames):
        # Generate sine wave
        value = amplitude * math.sin(2 * math.pi * frequency * i / sample_rate)
        # Apply envelope to avoid clicks
        envelope = 1.0
        if i < frames * 0.1:  # Fade in
            envelope = i / (frames * 0.1)
        elif i > frames * 0.9:  # Fade out
            envelope = (frames - i) / (frames * 0.1)
        
        tone.append(int(value * envelope * 32767))
    
    return tone

def create_cheerful_melody():
    """Create a cheerful wake-up melody"""
    sample_rate = 22050
    
    # Musical notes (frequencies in Hz)
    # Using major scale for cheerful sound
    notes = {
        'C4': 261.63,
        'D4': 293.66,
        'E4': 329.63,
        'F4': 349.23,
        'G4': 392.00,
        'A4': 440.00,
        'B4': 493.88,
        'C5': 523.25,
    }
    
    # Create a simple melody inspired by "Jaago jaago" pattern
    melody = [
        ('G4', 0.5),  # Jaa-
        ('A4', 0.5),  # go
        ('G4', 0.5),  # Jaa-
        ('A4', 0.5),  # go
        ('C5', 1.0),  # subh
        ('B4', 0.5),  # ho
        ('A4', 1.0),  # gyi
        ('G4', 0.3),  # (pause)
        ('A4', 0.3),
        ('B4', 0.3),
        ('C5', 1.5),  # Final cheerful note
    ]
    
    # Generate the complete sound
    complete_sound = []
    
    # Repeat the melody 3 times
    for repeat in range(3):
        for note, duration in melody:
            if note in notes:
                tone = generate_tone(notes[note], duration, sample_rate)
                complete_sound.extend(tone)
            
            # Add small pause between notes
            pause = generate_tone(0, 0.1, sample_rate, 0)
            complete_sound.extend(pause)
        
        # Add pause between repetitions
        if repeat < 2:
            pause = generate_tone(0, 0.5, sample_rate, 0)
            complete_sound.extend(pause)
    
    return complete_sound, sample_rate

def save_alarm_sound():
    """Generate and save the alarm sound"""
    try:
        print("Generating cheerful alarm sound...")
        sound_data, sample_rate = create_cheerful_melody()
        
        # Convert to bytes
        sound_array = array.array('h', sound_data)
        
        # Save as WAV file
        with wave.open('alarm_sound.wav', 'w') as wav_file:
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 2 bytes per sample
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(sound_array.tobytes())
        
        print("Alarm sound saved as 'alarm_sound.wav'")
        print(f"Duration: {len(sound_data) / sample_rate:.1f} seconds")
        
    except Exception as e:
        print(f"Error creating alarm sound: {e}")

if __name__ == "__main__":
    save_alarm_sound()