import random
import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import webbrowser as webBrowser
from plyer import notification
from pygame import mixer
import speedtest as speed


# Funny fallback responses
confusion_responses = [
    "I am not sure how to respond to that.",
    "Hmm… that went straight to the unknown dimension.",
    "Either you're a genius or I'm out of my league.",
    "That was as clear as mud to me.",
    "You just confused a robot. Congrats!",
    "I'm 99% artificial, 1% confused right now.",
    "I think you just asked the meaning of life.",
    "My brain's buffering… try again maybe?",
    "That input gave me a digital headache.",
    "Well, that short-circuited my logic board."
]


#password fro friday
for i in range(3):
    a=input("Enter Password to open Friday:-")
    password_file=open("password.txt")
    password=password_file.read()
    password_file.close()
    if(a==password):
     print("Welcome boss! PLZ speak [friday] to load me up")
     break
    elif(i==2 and a!=password):
        exit()
    elif(a!=password):
        print("try again")  
# from inro import play_gif
# play_gif()        
        
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

def alarm(query):
    timehere=open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("Alarm.py")
    

# Main loop
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if "friday" in query or "hello friday" in query or "hey friday" in query or "hi friday" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()

                if "go to sleep" in query:
                    speak("Going to sleep. Wake me up when you need me.")
                    break
                
                ################## Friday: the trilogy 2.O ####################
                elif "change password" in query:
                    speak("What's the new password\n")
                    new_pw=input("Enter the password")
                    new_pass= open("password.txt","w")
                    new_pass.write(new_pw)
                    new_pass.close()
                    speak("Done Boss")
                    speak(f"Your new password is{new_pw}")
                
                ##Schedule you day
                elif "schedule my day" in query:
                 tasks=[] #empty
                 speak("Do you want to clear old tasks (PLZ speak yes or no)") 
                 query=takeCommand().lower()
                 if "yes" in query:
                     file=open("tasks.txt","w")
                     file.write(f"")
                     file.close()
                     number_tasks=int(input("ENter the no. of tasks:-"))
                     i=0
                     for i in range(number_tasks):
                         tasks.append(input("Enter the tasks:- "))
                         file.open("tasks.txt","a")
                         file.write(f"{i}.{tasks[i]}\n")
                         file.close()
                 elif "no" in query:
                      i=0
                      number_tasks=int(input("ENter the no. of tasks:-"))
                
                      for i in range(number_tasks):
                         tasks.append(input("Enter the tasks:- "))
                         file=open("tasks.txt","a")
                         file.write(f"{i}.{tasks[i]}\n")
                         file.close()
                         
                elif "show my schedule" in query:
                     file=open("tasks.txt", "r")
                     content = file.read()
                     file.close()
                     mixer.init()
                     mixer.music.load("sound.mp3")
                     mixer.music.play()
                     notification.notify(
                         title="My schedule:- ",
                         message=content,
                         timeout=15
                     )  
                #############################################################
                
                #open apps better ways
                elif "open" in query or "launch" in query:
                    query = query.replace("open", "")
                    query = query.replace("launch", "")
                    query = query.replace("friday", "")
                    query = query.replace("app", "")
                    query = query.replace("application", "")
                    query = query.replace("the", "")
                    query = query.replace("my", "")
                    query = query.replace(" ", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                
                #speedTest
                elif "speed test" in query or "internet speed" in query:
                    wifi = speed.Speedtest()
                    upload_network = wifi.upload()/1048576
                    download_network = wifi.download()/1048576
                    print("upload speed is: ", upload_network, "Mbps")
                    print("download speed is: ", download_network, "Mbps")
                    speak(f"Upload speed is {upload_network} Mbps and download speed is {download_network} Mbps")
                    
                    #ipl score
                # elif "ipl score" in query or "ipl" in query:
                #     from plyer import notification
                #     import requests
                #     from bs4 import BeautifulSoup
                #     url = "https://www.cricbuzz.com/"
                #     page = requests.get(url)
                #     soup = BeautifulSoup(page.text, "html.parser")
                #     team1=soup.find_all("h2", class_="cb-col cb-col-100 cb-col-scores")[0].get_text()
                #     team2=soup.find_all("h2", class_="cb-col cb-col-100 cb-col-scores")[1].get_text()
                #     team1_score=soup.find_all(class_="cb-col cb-col-100")[8].get_text()
                #     team2_score=soup.find_all(class_="cb-col cb-col-100")[10].get_text()
                #     a=print(f"{team1}: {team1_score}")
                #     b=print(f"{team2}: {team2_score}")

                #     notification.notify(
                #         title="IPL Score",
                #         message=f"{team1}: {team1_score}\n{team2}: {team2_score}",
                #         timeout=10
                #     )
                
                
                ############## Focus Mode ##################
                elif "focus mode" in query or "do not disturb" in query:
                      try:
                         user_input = input("Are you sure you want to enable focus mode? -: [1 for YES / 2 for NO] ")
                         if not user_input.strip():
                            raise ValueError
                         a = int(user_input)
                      except ValueError:
                          speak("Invalid input. Focus mode not enabled.")
                          a = 2

                      if a == 1:
                            speak("Focus Mode is now enabled.")
                            os.startfile("D:\\jarves\\FocusMode.py")
    
                      else:
                          speak("Focus Mode not enabled.")
                ############## Focus Mode ##################
                ############## focus graph ##################
                elif "show my focus graph" in query or "focus graph" in query:
                    from Focus_graph import focus_graph
                    focus_graph()
                ############## focus graph ##################
                elif "translate" in query:
                    from translate import translate_text
                    query = query.replace("translate", "")
                    query = query.replace("friday", "")
                    translate_text(query)
                
                #game 
                elif "play game" in query or "game" in query:
                    from game import game_play
                    game_play()
                
                elif "screenshot" in query:
                    import pyautogui 
                    im=pyautogui.screenshot()
                    im.save("ss.jpg")
                
                elif "click photo" or "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("smile please")
                    pyautogui.press("enter")
                    
                
                elif "hello" in query or "hi" in query:
                    speak("Hello Boss! How are you today?")
                elif "i am fine" in query or "i am good" in query:
                    speak("That's great to hear!")
                elif "thank you" in query or "thanks" in query:
                    speak("You're welcome Boss")
                    
                    #music control
                elif "tired" in query or "bored" in query:
                    speak("playing some music for you")
                    a=(1,2,3,4,5)
                    b=random.choice(a)
                    if b==1:
                        webBrowser.open("https://www.youtube.com/watch?v=2Vv-BfVoq4g")
                    elif b==2:
                        webBrowser.open("https://www.youtube.com/watch?v=2Vv-BfVoq4g")
                    elif b==3:
                        webBrowser.open("https://www.youtube.com/watch?v=2Vv-BfVoq4g")       
                    elif b==4:
                        webBrowser.open("https://www.youtube.com/watch?v=2Vv-BfVoq4g")
                    elif b==5:
                        webBrowser.open("https://www.youtube.com/watch?v=2Vv-BfVoq4g")          
                #youtube control
                elif "pause" in query or "stop" in query:
                     pyautogui.press("k")
                     speak("paused")
                elif "play" in query:
                     pyautogui.press("k")
                     speak("playing") 
                elif "mute" in query:
                        pyautogui.press("m")
                        speak("muted")
                elif "volumeUp" in query: 
                       from keyboard import volumeUp
                       speak("turning volume up boss")
                       volumeUp()
                elif "volumeDown" in query:
                       from keyboard import volumeDown
                       speak("turning volume down boss")
                       volumeDown()             
                 #youtube control              
                elif "open" in query:
                     from Dictapp import openWebApp
                     openWebApp(query)
                       
                elif "close" in query:
                    from Dictapp import closeApp
                    closeApp(query)
                          
                #search 
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                    
                elif "youtube" in query or "search youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                    
                elif "wikipedia" in query or "search wikipedia" in query:  
                    from SearchNow import searchWikipedia
                    searchWikipedia(query) 
                    
                elif "chatGpt" in query or "search chatGpt" in query:
                    from SearchNow import searchChatgpt
                    searchChatgpt(query)
                    
                #news
                elif "news" in query or "latest news" in query:
                    from News import get_news   
                    get_news()
                        
                #calculator
                elif "calculator" in query or "calculate" in query:
                    from Calculator import wolframAlpha
                    from Calculator import calculator
                    query = query.replace("calculate", "")
                    query = query.replace("friday", "")
                    calculator(query)
                #send whatsapp message
                elif "whatsapp" in query or "send message" in query:
                    from Whatsapp import SendMessage
                    SendMessage()        
                #temperature            
                elif "temperature" in query or "weather" in query:
                    search="temperature in jaipur"
                    url=f"https://www.google.co.in/search?q={search}"
                    r=requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"The current {search} is {temp}")
                
                elif "set an alarm" in query or "set alarm" in query:
                    print("input time example: 10 and 30 and 10")
                    speak("Please tell me the time to set the alarm")
                    a= input("Set alarm time: ")
                    alarm(a)
                    speak("done boss!")
                    
                elif "time" in query or "what is the time" in query:
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"The time is {strTime}")
                    
                elif "finally sleep" in query:
                    speak("Going to sleep Boss!. Wake me up when you need me.")
                    exit()
                #Remember notes  
                elif "remember that" in query or "note" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("note", "")
                    rememberMessage = query.replace("remember", "")
                    rememberMessage = query.replace("write", "")
                    rememberMessage = query.replace("friday", "")
                    speak("Okay,."+rememberMessage)
                    rememberFile = open("remember.txt", "w")
                    rememberFile.write(rememberMessage)
                    rememberFile.close()
                elif "what do you remember" in query or "remember" in query:
                    rememberFile = open("remember.txt", "r")
                    speak("You told me " + rememberFile.read())
                    print("You told me " + rememberFile.read())
                
                elif "shutdown system" in query:
                    speak("Are you sure")   
                    shutdown=input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown=="yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown=="no":
                        break    
                 
                    
        else:   
                    speak(random.choice(confusion_responses))
