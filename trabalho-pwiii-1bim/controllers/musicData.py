import requests

def getAlbum(id):
    BASE_URL = "https://api.deezer.com/album/"
    
    try:
        r = requests.get(BASE_URL + id)
        albumData = r.json()
        
        return albumData
    
    except Exception as e:
        print(f"An error occured : {e}")
    

def getMusic(q):    
    BASE_URL = "https://api.deezer.com/search?q=" 
    try: 
        r = requests.get(BASE_URL+q)
        musicData = r.json()
        
        return musicData      
        
    except Exception as e:
        print(f"An error occurred: {e}")
        

def getPopularClassic():
    BASE_URL = "https://api.deezer.com/album/"
    try: 
        r = requests.get(BASE_URL+"1277074")
        musicData = r.json()
        
        return musicData      
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
def getPopularRock():
    BASE_URL = "https://api.deezer.com/album/"
    try: 
        r = requests.get(BASE_URL+"647938671")
        musicData = r.json()
        
        return musicData      
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
def getPopularForro():
    BASE_URL = "https://api.deezer.com/album/"
    try: 
        r = requests.get(BASE_URL+"704140461")
        musicData = r.json()
        
        return musicData      
        
    except Exception as e:
        print(f"An error occurred: {e}")
        

