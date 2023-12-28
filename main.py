from api_routes import app
import config

if __name__ == "__main__":

    def start_app(environ, start_response):
        """
        Start the application.

        :param environ: The environment dictionary.
        :param start_response: The start response function.
        """
        data = b"Hello, World!\n"
        start_response(
            "200 OK",
            [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))],
        )
        return iter([data])
