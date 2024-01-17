import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning Joel!")
        speak("Good Morning Joel!")
    elif hour >=12 and hour < 18:
        print("Good Afternoon Joel!")
        speak("Good Afternoon Joel!")
    else:
        print("Good evening Joel!")
        speak("Good Evening Joel!")
    print("I am Vincy")
    speak("I am Vincy")
    print("Please tell me how can I help you today?")
    speak("Please tell me how can I help you today")

def takeCommand():
    # It takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("joelkevindaniel@gmail.com", "joel@007")
    server.sendmail("joelkevindaniel@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'open wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            print("Opening YouTube...")
            speak(f"Opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            print("Opening Google...")
            speak(f"Opening google")
            webbrowser.open("google.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open stack overflow' in query:
            print("Opening Stack Overflow...")
            speak(f"Opening stack overflow")
            webbrowser.open("stackoverflow.com")
        elif 'open chat gpt' in query:
            webbrowser.open("chat.openai.com")
        elif 'play music' in query:
            music_dir = 'C:\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Hey, the Time is {strTime}")
            speak(f"Hey, the Time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\code_opencv"
            os.startfile(codePath)
        elif 'open photo' in query:
            photoPath = "C:\Album"
            os.startfile(photoPath)
        elif 'what is your name' in query:
            print("I am Gabriella. You can call me Gaby")
            speak(f"I am Gabriella. You can call me Gaby")
        elif 'who created you' in query:
            print("It is a secret. Only Joel knows that")
            speak(f"It is a secret. Only Joel knows that")
        elif 'will you marry me' in query:
            print("Sorry, I cannot do that. Anyways, thanks for your love")
            speak(f"Sorry, I cannot do that. Anyways, thanks for your love")
        elif 'how are you' in query:
            print("I am fine, Thank you")
            speak(f"I am fine, Thank you")
            print("How are you doing by the way?")
            speak(f"How are you doing by the way?")
        elif 'i am fine' in query:
            print("Good to know you are doing well.")
            speak(f"Good to know you are doing well.")
        elif 'email to dad' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "daniellawrencephilip@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")
