from flask import Flask
from database.setup import Base, db, Session
from url.controller import url_controller


Base.metadata.creat_all(db)

app = Flask(__name__)
app.register_blueprint(url_controller, url_prefix="/url")

if __name__ == "__main__":
    app.run(debug=True)

