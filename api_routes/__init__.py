from config import app
from api_routes import index, user, task

urls = {
    "/": index.Index.as_view("index"),
    "/login": index.Login.as_view("login"),
    "/task": task.TaskView.as_view("task"),
    "/logout": index.Logout.as_view("logout"),
}

for url, view in urls.items():
    app.add_url_rule(url, view_func=view)
