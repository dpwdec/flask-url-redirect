from flask import Flask
from url.controller import url_controller

app = Flask(__name__)
app.register_blueprint(url_controller, url_prefix="/url")

if __name__ == "__main__":
    app.run(debug=True)

