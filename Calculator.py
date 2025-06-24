import wolframalpha
import pyttsx3


# Initialize TTS engine
# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# engine.setProperty("rate", 190)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
from brianTTS import speak
def wolframAlpha(query):
   api_key="8GLJ44-XVY8G4KXP2"
   requester = wolframalpha.Client(api_key)
   requested = requester.query(query)
   
   try:
        answer = next(requested.results).text
        return answer
   except:
       speak("the value is not available")

def calculator(query):
    term=str(query)
    term=term.replace("friday", "")
    term=term.replace("multiply", "*")
    term=term.replace("plus", "+")
    term=term.replace("minus", "-") 
    term=term.replace("divide", "/")     
    
    final= str(term)
    try:
        result=wolframAlpha(final)
        print(f"Result: {result}")
        speak(f"The result is {result}")

    except:
        speak("Sorry Boss, I couldn't calculate that.")
        