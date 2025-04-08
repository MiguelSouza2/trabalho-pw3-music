from flask import render_template, request, redirect, url_for
from controllers import musicData



music = musicData.getMusic("summer")
musicTitle = music['data'][0]['title']
musicLink = music['data'][0]['link']
musicArtist = [
    music['data'][0]['artist']['name'], music['data'][0]['artist']['picture'] 
]
musicPreview = music['data'][0]['preview']


def init_app(app):
    @app.route("/")
    def home():
        
        return render_template("index.html",
                               musicTitle = musicTitle,
                               musicLink = musicLink, 
                               musicArtist = musicArtist,
                               musicPreview = musicPreview
                               )
        
        
    @app.route('/artistas')
    def artistas():
        return render_template('artistas.html')
    
        
    
   