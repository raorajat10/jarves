import requests
from bs4 import BeautifulSoup

def get_temperature():
    search = "temperature in jaipur"
    url = f"https://www.google.com/search?q={search}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    # Try all known possible class combinations Google has used
    temp_div = soup.find("div", class_="BNeawe iBp4i AP7Wnd")
    if not temp_div:
        # fallback (if Google changes the class again)
        temp_div = soup.find("span", class_="wob_t q8U8x")

    if temp_div:
        temp = temp_div.text
        print(f"The current temperature in Jaipur is {temp}")
    else:
        print("Sorry, I couldn't fetch the temperature.")
        # Optional: print HTML to debug
        print(soup.prettify())
