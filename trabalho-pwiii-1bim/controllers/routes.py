from flask import render_template, request, redirect, url_for
from controllers import musicData

# cadmusica
userlist = [{
    'Nome': '',
    'email': '',
    'Senha': ''
}]
playlist = []



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
        return render_template(
            "index.html",
            popularClassicMusics=popularClassicMusics,
            popularRockMusics=popularRockMusics,
            popularForroMusics=popularForroMusics
        )

    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        if request.method == 'POST':
            if request.form.get('Nome') and request.form.get('email') and request.form.get('Senha'):
                userlist.append({
                    'Nome': request.form.get('Nome'),
                    'email': request.form.get('email'),
                    'Senha': request.form.get('Senha')
                })
            return redirect(url_for('cadastro'))
        return render_template('cadastro.html', userlist=userlist)

    @app.route('/playlist', methods=['GET', 'POST'])
    def playlist_view():
        if request.method == 'POST':
            nome_musica = request.form.get('nome_musica')
            nome_artista = request.form.get('nome_artista')
            genero = request.form.get('genero')

            if nome_musica and nome_artista and genero:
                nova_musica = {
                    'nome_musica': nome_musica,
                    'nome_artista': nome_artista,
                    'genero': genero
                }
                playlist.append(nova_musica)

            return redirect(url_for('playlist_view'))

        return render_template('playlist.html', playlist=playlist)
    
    
    @app.route('/player', methods=['GET', 'POST'])
    def player():
        if request.method == 'POST':
            selectedMusic = request.form.get('music_id')
            selectedMusicTitle = request.form.get('music_title')

            if selectedMusic:
                searchMusic = musicData.getMusic(selectedMusicTitle)
                
                
                musicInfo = {
                    'title' : searchMusic['data'][0]['title'],
                    'link' : searchMusic['data'][0]['link'],
                    'preview' : searchMusic['data'][0]['preview'],
                    'duration' : searchMusic['data'][0]['duration'],
                    'artist' : searchMusic['data'][0]['artist'],
                    'album' : searchMusic['data'][0]['album']
                }
                return render_template(
                    'player.html',
                    musicInfo=musicInfo
                )
                
    @app.route('/base', methods=['GET', 'POST'])
    def baseSearch():
        if request.method == 'POST':
            search = request.form.get('search')
            if search:
                searchMusic = musicData.getMusic(search)
                musicInfo = {
                    'title': searchMusic['data'][0]['title'],
                    'link': searchMusic['data'][0]['link'],
                    'preview': searchMusic['data'][0]['preview'],
                    'duration': searchMusic['data'][0]['duration'],
                    'artist': searchMusic['data'][0]['artist'],
                    'album': searchMusic['data'][0]['album']
                }
                return render_template('player.html', musicInfo=musicInfo)
        

        return redirect(url_for('home'))
            
            
