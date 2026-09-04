from flask import Flask
from dotenv import load_dotenv
import os

from web import web_bp 
import web.routes

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(web_bp)

if __name__ == "__main__":
    app.run(debug=True)