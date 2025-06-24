import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import os


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source, 0, 4)
    try:
            print("Understanding...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}\n")
    except Exception as e:
            print("Sorry Boss, I didn't get that. Please repeat.")
            return "None"
    return query    
# query = takeCommand().lower()
# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# engine.setProperty("rate", 190)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
from brianTTS import speak    
#Google search      
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrape
        query = query.replace("friday", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        query = query.replace("search", "")
        query = query.replace("search google", "")
        query = query.replace("search with google", "")
        query = query.replace("search with", "")
        speak("this is what I found on google")
        
        try:
            pywhatkit.search(query)
            result = googleScrape.summary(query, 1)
            speak(result)
        except Exception as e:
            speak("Sorry Boss, I couldn't find anything on Google.")  
            
#Youtube search              
def searchYoutube(query):
    if "youtube" in query:
        speak("this is what I found on youtube")
        
        query = query.replace("friday", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("search", "")
        query = query.replace("search youtube", "")
        query = query.replace("search with youtube", "")
        query = query.replace("search with", "")
        
        web="https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)
        
        try:
            pywhatkit.playonyt(query)
            speak("Done Boss, I found this on Youtube")
        except Exception as e:
            print("Sorry Boss, I couldn't find anything on Youtube.")
            speak("Sorry Boss, I couldn't find anything on Youtube.") 
            
#Wikipedia search                   
def searchWikipedia(query):
    if "wikipedia" in query or "search wikipedia" in query:
        speak("Searching from wikipedia")
        query = query.replace("friday", "")
        query = query.replace("wikipedia search", "")
        query = query.replace("wikipedia", "")
        query = query.replace("search", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("search with wikipedia", "")
        query = query.replace("search with", "")
        
        
        try:
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        except Exception as e:
            print("Sorry Boss, I couldn't find anything on Wikipedia.")
            speak("Sorry Boss, I couldn't find anything on Wikipedia.") 
import openai

#openai.api_key = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")

def searchChatgpt(query):
    if "chatgpt" in query:
        speak("Searching with ChatGPT")
        query = query.replace("friday", "")
        query = query.replace("chatgpt search", "")
        query = query.replace("chatgpt", "")
        query = query.replace("search", "")
        query = query.replace("search chatgpt", "")
        query = query.replace("search with chatgpt", "")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": query}
                ],
                max_tokens=150
            )
            result = response["choices"][0]["message"]["content"]
            print(result)
            speak(result)
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry Boss, something went wrong while contacting ChatGPT.")
    