import requests
import json
import pyttsx3


# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# engine.setProperty("rate", 190)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
from brianTTS import speak   
def get_news(): 
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=9d5651a953cc466faae072cf3591e61e",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=9d5651a953cc466faae072cf3591e61e",
        "general": "https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey=9d5651a953cc466faae072cf3591e61e",
        "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=9d5651a953cc466faae072cf3591e61e",
        "science": "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=9d5651a953cc466faae072cf3591e61e",
        "sports": "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=9d5651a953cc466faae072cf3591e61e",
        "technology": "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=9d5651a953cc466faae072cf3591e61e",
        "top": "https://newsapi.org/v2/top-headlines?country=us&apiKey=9d5651a953cc466faae072cf3591e61e"
    }

    speak("Which category of news do you want to hear? {business, entertainment, general, health, science, sports, technology or top?}")
    field = input("Enter the category of news you want to hear: ")
    
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("URL found")
            break
        else:
            url= True
    if url == True:
        print("url not found")
    
    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news")
    
    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"Read more at: {news_url}")
    
        a = input("[Press 1 to continue] and [0 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "0":
            break

        speak("That's all for now. I hope you found the news interesting.")

        
        
       