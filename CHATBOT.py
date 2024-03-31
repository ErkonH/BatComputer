# \Users\Erick\CHATBOT_COMPUTER.py -- A chatbot program made with Python

# NO REAL TIME DATA

# pip install pyaudio
# pip install pipwin
# pip install SpeechRecognition
# pip install openai
# pip install pyttsx3

from openai import OpenAI
import pyttsx3
import speech_recognition as sr
import keyboard

# AUDIO AND SPEECH RECOGNITION
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)  
engine.setProperty('volume', 1)  

recognizer = sr.Recognizer()

# OPEN AI DATA
api_key = "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"
client = OpenAI(api_key=api_key)

# Function to handle key press
def on_key_press(event):
    global stop_value
    if event.name == '0':
        print("Program stopped by user.")
        stop_value = 1
        

# Register the key press event
keyboard.on_press(on_key_press)

# PROGRAM STARTS HERE
stop_value = 0  # Define stop_value globally
engine.say("Hello, I am an AI assistant. To use, say computer, then wait, then prompt your question.")
def chatbot():
    global stop_value
    
    while stop_value == 0:  # Check stop_value before proceeding
        try:
            with sr.Microphone() as source:
                print("Listening for 'computer'...")
                engine.say("Listening for computer")
                engine.runAndWait()
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            if "computer" in command:
                # Listen for question
                with sr.Microphone() as source:
                    print("Listening for the question...")
                    engine.say("What is your question?")
                    engine.runAndWait()
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                    question = recognizer.recognize_google(audio)
                    print("Question:", question)
                stream = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": question}],
                    stream=True,
                )
                response = ""
                for part in stream:
                    response += part.choices[0].delta.content or ""

                print(response)
                engine.say(response)
                engine.runAndWait()

            elif "vengeance" in command:
                # Listen for question
                with sr.Microphone() as source:
                    print("ACCESS GRANTED, Hello Batman, how may I assist you?")
                    engine.say("ACCESS GRANTED, Hello Batman, how may I assist you?")
                    engine.runAndWait()
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                    question = recognizer.recognize_google(audio)
                    print("Question:", question)

                stream = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": question}],
                    stream=True,
                )
                response = ""
                for part in stream:
                    response += part.choices[0].delta.content or ""

                print(response)
                engine.say(response)
                engine.runAndWait()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Main program
value = True
while value:
    chatbot()
