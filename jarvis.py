import os
import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr

# ---------- Voice (Text to Speech) ----------
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ---------- Commands ----------
def run_command(text):
    t = text.lower()

    # Open Scaler School of Technology (ONLY exact command)
    if t == "open scaler school of technology":
        webbrowser.open("https://sst.scaler.com")
        return "Opening Scaler School of Technology website, Sir."

    # Open Google
    elif "open google" in t:
        webbrowser.open("https://www.google.com")
        return "Opening Google, Sir."

    # Open YouTube
    elif "open youtube" in t:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube, Sir."

    # Open Google
    if t == "open google":
        webbrowser.open("https://www.google.com")
        return "Opening Google, Sir."

    # Open Scaler School of Technology (SST)
    if t in ["open sst", "open scaler school of technology"]:
        webbrowser.open("https://www.scaler.com")
        return "Opening Scaler School of Technology website, Sir."

    # Google Search (only when user says "search ...")
    if t.startswith("search "):
        query = t.replace("search", "", 1).strip()
        if query:
            webbrowser.open(
                f"https://www.google.com/search?q={query.replace(' ', '+')}"
            )

    # Time
    elif "time" in t:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"It is {now}, Sir."

    # Calculator
    elif "calculator" in t:
        os.startfile("calc.exe")
        return "Opening calculator, Sir."

    # Exit
    elif "exit" in t or "quit" in t:
        return "EXIT"

    return None

# ---------- Speech Recognition ----------
r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎙 Speak now...")
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text
    except:
        return ""

# ---------- Main ----------
speak(
    "Jarvis is online and ready, Sir. "
    "Say open google, open youtube, sst, search something, time, calculator, or exit."
)

while True:
    user_text = listen()

    if not user_text:
        speak("I did not hear that, Sir.")
        continue

    result = run_command(user_text)

    if result == "EXIT":
        speak("Goodbye, Sir.")
        break
    elif result:
        speak(result)
    else:
        speak("I can only do basic commands right now, Sir.")
