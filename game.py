import pyttsx3
import speech_recognition
import random

# Initialize TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take voice command
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
def game_play():
    speak("Welcome to the game of rock, paper, scissors")
    speak("You will play against the computer")
    speak("be ready to play")
    print("let's playyyyyyyy")
    
    me_score = 0
    comp_score = 0
    i = 0
    
    while(i < 5):
        choose = ["rock", "paper", "scissors"]
        comp_choice = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
          if (comp_choice == "rock"):
              speak("rock")
              print(f"Score:- me:- {me_score} comp: {comp_score}")
          elif (comp_choice == "paper"):
              speak("paper")
              comp_score += 1
              print(f"Score:- me:- {me_score} comp: {comp_score}")    
          else:
              speak("scissors")
              me_score += 1
              print(f"Score:- me:- {me_score} comp: {comp_score}")
        elif (query == "paper"):
          if (comp_choice == "rock"):
              speak("rock")
              me_score += 1
              print(f"Score:- me:- {me_score} comp: {comp_score}")
          elif (comp_choice == "paper"):
              speak("paper")
              print(f"Score:- me:- {me_score} comp: {comp_score}")
          else:
              speak("scissors")
              comp_score += 1
              print(f"Score:- me:- {me_score} comp: {comp_score}")      
        elif (query == "scissors"or query == "scissor" or query == "cissor" or query == "cissors" or query == "ceasar"):
          if (comp_choice == "rock"):
              speak("rock")
              comp_score += 1
              print(f"Score:- me:- {me_score} comp: {comp_score}")
          elif (comp_choice == "paper"):
              speak("paper")
              me_score += 1
              print(f"Score:- me:- {me_score} comp: {comp_score}")
          else:
              speak("scissors")
              print(f"Score:- me:- {me_score} comp: {comp_score}")      
        i += 1
    
    print(f"Final Score:- me:- {me_score} comp: {comp_score}")
    if (me_score > comp_score):
        speak("You win")
    elif (me_score < comp_score):
        speak("You lose")
    else:
        speak("It's a tie")          