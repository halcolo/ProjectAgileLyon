from api_routes import app
import config

if __name__ == "__main__":
    
    def app(environ, start_response):
        data = b"Hello, World!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
    # app.run(debug=True, port=config.PORT)
