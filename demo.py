#!/usr/bin/env python3
"""
Demo script for the Cute Cat Alarm Clock
Shows off the key features and plays the alarm sound
"""

import os
import time
import pygame

def demo_alarm_sound():
    """Demonstrate the alarm sound"""
    print("🎵 Playing alarm sound demo...")
    print("   This is the custom 'Jaago jaago subh ho gyi' inspired melody!")
    
    if os.path.exists('alarm_sound.wav'):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load('alarm_sound.wav')
            pygame.mixer.music.play()
            
            print("   ♪ Playing... (Press Ctrl+C to stop)")
            
            # Play for a few seconds
            time.sleep(10)
            pygame.mixer.music.stop()
            print("   ✓ Demo complete!")
            
        except Exception as e:
            print(f"   ❌ Error playing sound: {e}")
    else:
        print("   ❌ Alarm sound file not found. Run 'python create_alarm_sound.py' first.")

def show_features():
    """Display the alarm clock features"""
    print("\n🐱 Cute Cat Alarm Clock Features:")
    print("=" * 50)
    print("🎨 Beautiful GUI with cute cat background")
    print("⏰ Real-time digital clock display")
    print("📅 Current date display")
    print("🔔 Easy alarm setting with spinboxes")
    print("🎵 Custom 'Jaago jaago subh ho gyi' alarm melody")
    print("🛑 Alarm control buttons (Set/Cancel/Test/Stop)")
    print("🎪 Attractive and user-friendly interface")
    print("🌐 Auto-downloads cute cat background image")
    print("🎯 Modal alarm popup when alarm rings")
    print("🔊 Audio feedback and system integration")
    print("=" * 50)

def main():
    """Main demo function"""
    print("🐱 Welcome to the Cute Cat Alarm Clock Demo! 🐱")
    print()
    
    show_features()
    
    print("\nWould you like to:")
    print("1. 🎵 Play alarm sound demo")
    print("2. 🚀 Launch the full alarm clock GUI")
    print("3. 📖 View README instructions")
    print("4. ❌ Exit")
    
    try:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            demo_alarm_sound()
        elif choice == "2":
            print("\n🚀 Launching alarm clock GUI...")
            os.system("python alarm_clock.py")
        elif choice == "3":
            if os.path.exists("README.md"):
                print("\n📖 README Contents:")
                print("=" * 50)
                with open("README.md", "r") as f:
                    print(f.read()[:1000] + "...")
                print("=" * 50)
                print("(See README.md for complete instructions)")
            else:
                print("❌ README.md not found")
        elif choice == "4":
            print("👋 Goodbye! Sweet dreams!")
        else:
            print("❌ Invalid choice. Please run the demo again.")
            
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted. Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()