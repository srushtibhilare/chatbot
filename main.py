import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def chatbot_response(command):
    command = command.lower()   

    if "hello" in command:
        return "Hello! How can I assist you today?"
    elif "how are you" in command:
        return "I'm just a program, but I'm functioning perfectly. How can I help you?"
    elif "your name" in command:
        return "I'm your voice assistant!"
    elif "open google" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
        return "I have opened Google for you."
    elif "open Youtube" in command: 
        speak("Opening youtube...")
        webbrowser.open("https://www.youtube.com/")
        return "I have opened Youtube for you."
    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        return "I'm sorry, I didn't understand that. Please try again."

if __name__ == "__main__":  
    speak("Hey sir, how may I help you?")

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source) 
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)  
                print(f"You said: {command}")
                
                response = chatbot_response(command)
                print(response)
                speak(response)

            except sr.UnknownValueError:
                print("Sorry, I couldn't understand what you said.")
                speak("Sorry, I couldn't understand what you said.")
            except sr.RequestError as e:
                print(f"Request error; {e}")
                speak("I couldn't connect to the speech recognition service. Please check your internet connection.")
