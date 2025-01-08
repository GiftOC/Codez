import speech_recognition as sr
import pyttsx3

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input."""
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Sorry, I'm having trouble connecting to the service."

# Test the basic voice interaction
speak("Hello, how can I assist you?")
user_input = listen()
print(f"You said: {user_input}")

from transformers import pipeline

# Initialize the conversational AI model
chat_model = pipeline("text-generation", model="gpt2")

def generate_response(user_input):
    """Generate a response from the AI."""
    response = chat_model(user_input, max_length=50)[0]["generated_text"]
    return response

# Test the AI response
ai_response = generate_response("Hello AI, how are you?")
print(f"AI: {ai_response}")

import json
from datetime import datetime

# Folder to save conversations
SAVE_FOLDER = "conversations/"

def save_conversation(user_input, ai_response):
    """Save conversation to a file."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    data = {"timestamp": timestamp, "user": user_input, "ai": ai_response}
    with open(f"{SAVE_FOLDER}conversation_{timestamp}.json", "w") as file:
        json.dump(data, file, indent=4)

# Example usage
save_conversation("Hello AI!", "Hello! How can I assist you?")

import speech_recognition as sr
import pyttsx3
import json
from datetime import datetime
from transformers import pipeline

# Initialize recognizer, TTS engine, and AI model
recognizer = sr.Recognizer()
engine = pyttsx3.init()
chat_model = pipeline("text-generation", model="gpt2")

# Folder to save conversations
SAVE_FOLDER = "conversations/"

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input."""
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Sorry, I'm having trouble connecting to the service."

def generate_response(user_input):
    """Generate a response from the AI."""
    response = chat_model(user_input, max_length=50)[0]["generated_text"]
    return response

def save_conversation(user_input, ai_response):
    """Save conversation to a file."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    data = {"timestamp": timestamp, "user": user_input, "ai": ai_response}
    with open(f"{SAVE_FOLDER}conversation_{timestamp}.json", "w") as file:
        json.dump(data, file, indent=4)

def main():
    print("AI is ready to chat!")
    speak("Hello, I'm ready to chat!")
    while True:
        user_input = listen()
        if user_input.lower() in ["exit", "quit"]:
            speak("Goodbye!")
            break
        print(f"You: {user_input}")
        ai_response = generate_response(user_input)
        print(f"AI: {ai_response}")
        speak(ai_response)
        save_conversation(user_input, ai_response)

if __name__ == "__main__":
    import os
    os.makedirs(SAVE_FOLDER, exist_ok=True)
    main()
