import json
import requests
import time
from newsapi import NewsApiClient

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)

newsapi = NewsApiClient(api_key='ae3a2ade838a47ecabd3d7d5400cb9ab')
#source = newsapi.get_sources()
#print(source)
get_r = requests.get('http://newsapi.org/v2/everything?q=Pakistan&apiKey=ae3a2ade838a47ecabd3d7d5400cb9ab')
var_text = get_r.text
parsedData = json.loads(var_text)

for i in range(2):
    print(parsedData['articles'][i]['title'])
    speak(parsedData['articles'][i]['title'])
    time.sleep(1)
    speak(parsedData['articles'][i]['description'])
    time.sleep(2)
myMessage="Thank you for listening news Mr.Hammmad"
speak(myMessage)
