from flask import render_template, request, redirect, url_for
from controllers import musicData

# cadmusica
userlist = [{
        'Nome' : '',
        'email' : '',
        'Senha' :''
            
        }]



music = musicData.getMusic("era um garoto como eu")
musicTitle = music['data'][0]['title']
musicLink = music['data'][0]['link']
musicArtist = [
    music['data'][0]['artist']['name'], music['data'][0]['artist']['picture'] 
]
musicPreview = music['data'][0]['preview']

# cadmusica end

# getmusica

newClassic = musicData.getPopularClassic()
popularClassicMusics = []
for i in range(3):
    popularClassicMusics.append(newClassic['tracks']['data'][i])
    
newRock = musicData.getPopularRock()
popularRockMusics = []
for i in range(3):
    popularRockMusics.append(newRock['tracks']['data'][i])

newForro = musicData.getPopularForro()
popularForroMusics = []
for i in range(3):
    popularForroMusics.append(newForro['tracks']['data'][i])

# getmusica end



def init_app(app):
    @app.route("/")
    def home():
        
        return render_template("index.html",
                               popularClassicMusics=popularClassicMusics,
                               popularRockMusics=popularRockMusics,
                               popularForroMusics=popularForroMusics
                               )
    
    @app.route('/cadmusica', methods=['GET', 'POST'])
    def cadmusica():
        if request.method == 'POST':
            if request.form.get('Nome') and request.form.get('email') and request.form.get('Senha'):
                userlist.append({'Nome': request.form.get('Nome'), 'email' : request.form.get('email'), 'Senha': request.form.get('Senha')})
            return redirect(url_for('cadmusica'))
        return render_template('cadmusica.html',
                               userlist=userlist)
   