import requests
import pygame
import time
import tempfile
import os

def speak(text):
    print(f"JARVIS: {text}")
    try:
        # Add slight delay for natural flow
        time.sleep(0.8)

        # Fetch the audio from the API
        url = f"https://api.streamelements.com/kappa/v2/speech?voice=Brian&text={text}"
        response = requests.get(url)

        if response.status_code != 200:
            print("❌ Error: Failed to fetch audio from TTS API.")
            return

        # Create temporary MP3 file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_file.write(response.content)
            temp_path = temp_file.name

        # Play the audio
        pygame.mixer.init()
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        # Clean up
        pygame.mixer.quit()
        os.remove(temp_path)

    except Exception as e:
        print("❌ Error in TTS:", e)
