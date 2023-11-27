from config import app
from api_routes import (views, 
                        user, 
                        game)

# app.add_url_rule('/', view_func=views.Index.as_view('index'))
# app.add_url_rule('/login', view_func=views.Login.as_view('login'))
# app.add_url_rule('/game', view_func=game.GameView.as_view('game'))
# app.add_url_rule('/logout', view_func=views.Logout.as_view('logout'))

# Register view
urls = {
    '/': views.Index.as_view('index'),
    '/login': views.Login.as_view('login'),
    '/game': game.GameView.as_view('game'),
    '/logout': views.Logout.as_view('logout')
}

for url, view in urls.items():
    app.add_url_rule(url, view_func=view)