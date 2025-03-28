from flask import Flask
from users import Authentication
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(Authentication,url_prefix = '/api')

if __name__ == "__main__":
    app.run(debug=True)