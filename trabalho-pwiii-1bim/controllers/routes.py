from flask import render_template, request, redirect, url_for
from controllers import musicData


# music = musicData.getMusic("era um garoto como eu")
# musicTitle = music['data'][0]['title']
# musicLink = music['data'][0]['link']
# musicArtist = [
#     music['data'][0]['artist']['name'], music['data'][0]['artist']['picture'] 
# ]
# musicPreview = music['data'][0]['preview']

newClassic = musicData.getPopularClassic()
popularClassicMusics = []
for i in range(3):
    popularClassicMusics.append(newClassic['tracks']['data'][i])
    
newRock = musicData.getPopularRock()
popularRockMusics = []
for i in range(3):
    popularRockMusics.append(newRock['tracks']['data'][i])

# newForro = musicData.getPopularForro()
# popularForroMusics = []
# for i in range(3):
#     popularForroMusics.append(newForro['tracks']['data'][i])

print(popularRockMusics)

def init_app(app):
    @app.route("/")
    def home():
        
        return render_template("index.html",
                               popularClassicMusics=popularClassicMusics,
                               popularRockMusics=popularRockMusics,
                               )
    
   