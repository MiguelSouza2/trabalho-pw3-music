from flask import render_template, request, redirect, url_for
from controllers import musicData
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



def init_app(app):
    @app.route("/")
    def home():
        
        return render_template("index.html",
                               musicTitle = musicTitle,
                               musicLink = musicLink, 
                               musicArtist = musicArtist,
                               musicPreview = musicPreview
                               )
        
    @app.route('/cadmusica', methods=['GET', 'POST'])
    def cadmusica():
        if request.method == 'POST':
            if request.form.get('Nome') and request.form.get('email') and request.form.get('Senha'):
                userlist.append({'Nome': request.form.get('Nome'), 'email' : request.form.get('email'), 'Senha': request.form.get('Senha')})
            return redirect(url_for('cadmusica'))
        return render_template('cadmusica.html',
                               userlist=userlist)
   