import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    print("Initializing microphone...")
    with sr.Microphone() as source:
        print("Microphone initialized.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError as e:
            print("Request error from Google Speech Recognition service:", e)
            return ""
        except Exception as e:
            print("Error:", e)
            return ""


# Function to handle commands
def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)
    elif "date" in command:
        current_date = datetime.date.today().strftime("%B %d, %Y")
        speak("Today's date is " + current_date)
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            url = "https://www.google.com/search?q=" + query
            webbrowser.open(url)
            speak("Here are the search results for " + query)
        else:
            speak("What would you like me to search for?")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I didn't understand that.")

# Main function
if __name__ == "__main__":
    speak("Hi there! I'm your voice assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            handle_command(command)
