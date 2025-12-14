# imports depends
import sys
import os
from colorama import Fore, Style, init
from openrouter import OpenRouter

init()
os.system('cls')
print(Fore.MAGENTA + """
dP                         dP                oo    d888888P dP     dP dP 
88                         88                         88    88     88 88 
88d888b. .d8888b. .d8888b. 88  .dP  .d8888b. dP       88    88     88 88 
88'  `88 88'  `88 88'  `"" 88888"   88'  `88 88       88    88     88 88 
88    88 88.  .88 88.  ... 88  `8b. 88.  .88 88       88    Y8.   .8P 88 
dP    dP `88888P8 `88888P' dP   `YP `88888P8 dP       dP    `Y88888P' dP 
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
""")
print(Fore.CYAN + Style.BRIGHT + "developed by ionixv, made possible by hack club" + Style.RESET_ALL)
print()

# sets the server url and api key
client = OpenRouter(
    api_key="YOUR_API_KEY_GOES_HERE",
    server_url="https://ai.hackclub.com/proxy/v1",
)

# defines the request function, this asks the ai the question
def send(request):
    response = client.chat.send(
    model="moonshotai/kimi-k2-0905",
    messages=[
        {"role": "user", "content": request}
    ],
    stream=False,
    )
    print(response.choices[0].message.content)

# defines the userside function, this is what the user interacts with
def askusr():
    print(Fore.GREEN + "Hey there, what do you wanna ask AI today?" + Fore.WHITE)
    request = input()
    os.system('cls')
    print(Fore.BLUE + "Generation will be below this text. -------------------------------")
    print(Fore.WHITE)
    send("Please make sure your output is terminal friendly, NO MARKDOWN FORMATTING! The user says: " + request)
    res()

# defines the restart function, asks the user if they wish to ask another question
def res():
    print()
    print(Fore.YELLOW + "Another question? (y/n)")
    restart = input()
    if restart == "y":
        askusr()
        sys.os('cls')
    else:
        sys.exit()

# starts the cycle
askusr()