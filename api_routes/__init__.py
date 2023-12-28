from config import app
from api_routes import index, player, task, error, login, singin


urls = {
    "/": index.Index.as_view("index"),
    "/login": login.Login.as_view("login"),
    "/task": task.TaskView.as_view("task"),
    "/logout": index.Logout.as_view("logout"),
    "/signin": singin.Signin.as_view("signin"),
}

for url, view in urls.items():
    app.add_url_rule(url, view_func=view)
