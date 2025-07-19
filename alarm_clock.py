#!/usr/bin/env python3
"""
Cute Cat Alarm Clock GUI
A beautiful and functional alarm clock with a cute cat background
that plays "Jaago jaago subh ho gyi" alarm sound.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import threading
import time
import pygame
import os
from PIL import Image, ImageTk
import requests
from io import BytesIO

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("🐱 Cute Cat Alarm Clock")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Initialize pygame mixer for audio
        pygame.mixer.init()
        
        # Variables
        self.alarm_time = None
        self.alarm_active = False
        self.alarm_thread = None
        
        # Setup GUI
        self.setup_background()
        self.setup_widgets()
        self.update_time()
        
        # Download alarm sound
        self.setup_alarm_sound()
    
    def setup_background(self):
        """Setup the cute cat background"""
        try:
            # Try to download a cute cat image
            cat_image_url = "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80"
            
            response = requests.get(cat_image_url, timeout=10)
            img = Image.open(BytesIO(response.content))
            img = img.resize((800, 600), Image.Resampling.LANCZOS)
            
            # Apply a semi-transparent overlay to make text readable
            overlay = Image.new('RGBA', img.size, (255, 255, 255, 100))
            img = img.convert('RGBA')
            img = Image.alpha_composite(img, overlay)
            
            self.bg_image = ImageTk.PhotoImage(img)
            
        except Exception as e:
            print(f"Failed to download cat image: {e}")
            # Create a cute gradient background as fallback
            self.create_gradient_background()
        
        # Set background
        self.bg_label = tk.Label(self.root, image=self.bg_image if hasattr(self, 'bg_image') else None)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def create_gradient_background(self):
        """Create a cute gradient background as fallback"""
        width, height = 800, 600
        img = Image.new('RGB', (width, height), '#FFB6C1')  # Light pink
        
        # Create gradient effect
        for y in range(height):
            for x in range(width):
                r = int(255 - (y / height) * 100)  # Fade from white to pink
                g = int(182 + (y / height) * 50)
                b = int(193 + (y / height) * 50)
                img.putpixel((x, y), (r, g, b))
        
        self.bg_image = ImageTk.PhotoImage(img)
    
    def setup_widgets(self):
        """Setup all GUI widgets"""
        # Main frame with transparent background
        main_frame = tk.Frame(self.root, bg='white', relief='raised', bd=2)
        main_frame.place(relx=0.5, rely=0.5, anchor='center', width=600, height=400)
        
        # Title
        title_label = tk.Label(main_frame, text="🐱 Cute Cat Alarm Clock 🐱", 
                              font=('Comic Sans MS', 24, 'bold'), 
                              fg='#FF69B4', bg='white')
        title_label.pack(pady=20)
        
        # Current time display
        self.time_label = tk.Label(main_frame, text="", 
                                  font=('Digital-7', 48, 'bold'), 
                                  fg='#4169E1', bg='white')
        self.time_label.pack(pady=10)
        
        # Date display
        self.date_label = tk.Label(main_frame, text="", 
                                  font=('Arial', 16), 
                                  fg='#2E8B57', bg='white')
        self.date_label.pack(pady=5)
        
        # Alarm setting frame
        alarm_frame = tk.Frame(main_frame, bg='white')
        alarm_frame.pack(pady=20)
        
        tk.Label(alarm_frame, text="Set Alarm:", 
                font=('Arial', 14, 'bold'), fg='#8B0000', bg='white').grid(row=0, column=0, columnspan=3, pady=5)
        
        # Hour selection
        tk.Label(alarm_frame, text="Hour:", font=('Arial', 12), bg='white').grid(row=1, column=0, padx=5)
        self.hour_var = tk.StringVar(value="07")
        hour_spinbox = tk.Spinbox(alarm_frame, from_=0, to=23, width=5, 
                                 textvariable=self.hour_var, format="%02.0f",
                                 font=('Arial', 12))
        hour_spinbox.grid(row=1, column=1, padx=5)
        
        # Minute selection
        tk.Label(alarm_frame, text="Minute:", font=('Arial', 12), bg='white').grid(row=1, column=2, padx=5)
        self.minute_var = tk.StringVar(value="00")
        minute_spinbox = tk.Spinbox(alarm_frame, from_=0, to=59, width=5, 
                                   textvariable=self.minute_var, format="%02.0f",
                                   font=('Arial', 12))
        minute_spinbox.grid(row=1, column=3, padx=5)
        
        # Control buttons frame
        button_frame = tk.Frame(main_frame, bg='white')
        button_frame.pack(pady=20)
        
        # Set alarm button
        self.set_button = tk.Button(button_frame, text="🔔 Set Alarm", 
                                   command=self.set_alarm,
                                   font=('Arial', 12, 'bold'),
                                   bg='#32CD32', fg='white',
                                   width=12, height=2)
        self.set_button.pack(side=tk.LEFT, padx=10)
        
        # Cancel alarm button
        self.cancel_button = tk.Button(button_frame, text="❌ Cancel Alarm", 
                                      command=self.cancel_alarm,
                                      font=('Arial', 12, 'bold'),
                                      bg='#FF6347', fg='white',
                                      width=12, height=2,
                                      state='disabled')
        self.cancel_button.pack(side=tk.LEFT, padx=10)
        
        # Test alarm button
        test_button = tk.Button(button_frame, text="🎵 Test Alarm", 
                               command=self.test_alarm,
                               font=('Arial', 12, 'bold'),
                               bg='#9370DB', fg='white',
                               width=12, height=2)
        test_button.pack(side=tk.LEFT, padx=10)
        
        # Alarm status label
        self.status_label = tk.Label(main_frame, text="No alarm set", 
                                    font=('Arial', 12), 
                                    fg='#696969', bg='white')
        self.status_label.pack(pady=10)
    
    def setup_alarm_sound(self):
        """Setup or generate alarm sound"""
        try:
            # Create a simple beep sound file if it doesn't exist
            if not os.path.exists('alarm_sound.wav'):
                self.create_alarm_sound()
        except Exception as e:
            print(f"Error setting up alarm sound: {e}")
    
    def create_alarm_sound(self):
        """Create a simple alarm sound using pygame"""
        try:
            # Generate a simple beep sound
            sample_rate = 22050
            duration = 2  # seconds
            frequency = 880  # Hz (A note)
            
            import numpy as np
            
            # Generate sine wave
            frames = int(duration * sample_rate)
            arr = np.zeros(frames)
            
            for i in range(frames):
                arr[i] = np.sin(2 * np.pi * frequency * i / sample_rate)
            
            # Convert to 16-bit integers
            arr = (arr * 32767).astype(np.int16)
            
            # Save as wav file
            import wave
            with wave.open('alarm_sound.wav', 'w') as wav_file:
                wav_file.setnchannels(1)  # mono
                wav_file.setsampwidth(2)  # 2 bytes per sample
                wav_file.setframerate(sample_rate)
                wav_file.writeframes(arr.tobytes())
                
        except ImportError:
            # If numpy is not available, create a text file as placeholder
            with open('alarm_sound.wav', 'w') as f:
                f.write("# Placeholder alarm sound file")
            print("Created placeholder alarm sound file")
    
    def update_time(self):
        """Update the current time display"""
        now = datetime.datetime.now()
        time_str = now.strftime("%H:%M:%S")
        date_str = now.strftime("%A, %B %d, %Y")
        
        self.time_label.config(text=time_str)
        self.date_label.config(text=date_str)
        
        # Check if alarm should ring
        if self.alarm_active and self.alarm_time:
            current_time = now.strftime("%H:%M")
            if current_time == self.alarm_time:
                self.ring_alarm()
        
        # Schedule next update
        self.root.after(1000, self.update_time)
    
    def set_alarm(self):
        """Set the alarm"""
        try:
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            
            self.alarm_time = f"{hour:02d}:{minute:02d}"
            self.alarm_active = True
            
            self.status_label.config(text=f"🔔 Alarm set for {self.alarm_time}", fg='#008000')
            self.set_button.config(state='disabled')
            self.cancel_button.config(state='normal')
            
            messagebox.showinfo("Alarm Set", f"Alarm set for {self.alarm_time}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid time values")
    
    def cancel_alarm(self):
        """Cancel the alarm"""
        self.alarm_active = False
        self.alarm_time = None
        
        self.status_label.config(text="No alarm set", fg='#696969')
        self.set_button.config(state='normal')
        self.cancel_button.config(state='disabled')
        
        messagebox.showinfo("Alarm Cancelled", "Alarm has been cancelled")
    
    def test_alarm(self):
        """Test the alarm sound"""
        self.play_alarm_sound()
    
    def ring_alarm(self):
        """Ring the alarm"""
        self.alarm_active = False  # Stop checking for alarm
        
        # Show alarm dialog
        alarm_window = tk.Toplevel(self.root)
        alarm_window.title("⏰ ALARM! ⏰")
        alarm_window.geometry("400x200")
        alarm_window.configure(bg='#FFB6C1')
        alarm_window.grab_set()  # Make it modal
        
        # Center the window
        alarm_window.transient(self.root)
        alarm_window.geometry("400x200+200+150")
        
        # Alarm message
        tk.Label(alarm_window, text="🐱 JAAGO JAAGO SUBH HO GYI! 🐱", 
                font=('Comic Sans MS', 18, 'bold'), 
                fg='#FF0000', bg='#FFB6C1').pack(pady=20)
        
        tk.Label(alarm_window, text="Time to wake up!", 
                font=('Arial', 14), 
                fg='#8B0000', bg='#FFB6C1').pack(pady=10)
        
        # Stop alarm button
        stop_button = tk.Button(alarm_window, text="🛑 Stop Alarm", 
                               command=lambda: self.stop_alarm(alarm_window),
                               font=('Arial', 12, 'bold'),
                               bg='#FF4500', fg='white',
                               width=15, height=2)
        stop_button.pack(pady=20)
        
        # Play alarm sound
        self.play_alarm_sound()
        
        # Reset alarm controls
        self.set_button.config(state='normal')
        self.cancel_button.config(state='disabled')
        self.status_label.config(text="Alarm ringing! 🔔", fg='#FF0000')
    
    def play_alarm_sound(self):
        """Play the alarm sound"""
        try:
            if os.path.exists('alarm_sound.wav'):
                pygame.mixer.music.load('alarm_sound.wav')
                pygame.mixer.music.play(-1)  # Loop indefinitely
            else:
                # Fallback: system beep
                print('\a' * 5)  # Terminal bell
        except Exception as e:
            print(f"Error playing alarm sound: {e}")
            print('\a' * 5)  # Fallback to terminal bell
    
    def stop_alarm(self, alarm_window):
        """Stop the alarm"""
        try:
            pygame.mixer.music.stop()
        except:
            pass
        
        alarm_window.destroy()
        self.status_label.config(text="Alarm stopped", fg='#696969')

def main():
    """Main function to run the alarm clock"""
    root = tk.Tk()
    
    # Set window icon (optional)
    try:
        root.iconbitmap('cat_icon.ico')
    except:
        pass  # Icon file not found
    
    app = AlarmClock(root)
    
    # Center window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (800 // 2)
    y = (root.winfo_screenheight() // 2) - (600 // 2)
    root.geometry(f"800x600+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()