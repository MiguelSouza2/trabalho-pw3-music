import requests

BASE_URL = "https://api.deezer.com/search?q="
query = "lafoule"

def getMusic(q):     
    try: 
        r = requests.get(BASE_URL+q)
        musicData = r.json()
        
        return musicData      
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
  