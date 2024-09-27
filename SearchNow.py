import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold =300
        audio = r.listen(source,0,4)

    try:
        print("understanding...")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said : {query}\n")
    except Exception as e :
        print("say that again")
        return "None"
    return query

query = takecommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("Sara","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what is found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what i found for your search !")
        query = query.replace("Sara","")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching From wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("Sara","")

        results = wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia..")
        print(results)
        speak(results)