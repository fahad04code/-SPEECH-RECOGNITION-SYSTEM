import speech_recognition as sr
import os
from pathlib import Path

def transcribe_audio(audio_file_path):
    """
    Transcribes an audio file (WAV format) to text using Google Speech Recognition.
    
    Args:
        audio_file_path (str): Path to the WAV audio file
        
    Returns:
        str: Transcribed text or error message
    """
    # Check if file exists and is a WAV file
    if not os.path.exists(audio_file_path):
        return "Error: Audio file not found"
    if not audio_file_path.lower().endswith('.wav'):
        return "Error: Please provide a WAV audio file"

    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Load audio file
    try:
        with sr.AudioFile(audio_file_path) as source:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            # Record the audio
            audio = recognizer.record(source)
            
        # Attempt to transcribe
        try:
            transcription = recognizer.recognize_google(audio)
            return transcription
        except sr.UnknownValueError:
            return "Error: Could not understand the audio"
        except sr.RequestError as e:
            return f"Error: Could not request results; {e}"
            
    except Exception as e:
        return f"Error: Failed to process audio file; {e}"

def main():
    # Example usage
    audio_file = "converted_audio_16k.wav"  # Replace with your WAV file path
    result = transcribe_audio(audio_file)
    print("Transcription:", result)

if __name__ == "__main__":
    main()
