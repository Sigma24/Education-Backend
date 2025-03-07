from flask import Flask
from users import Register_user
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(Register_user,url_prefix = '/api')

if __name__ == "__main__":
    app.run(debug=True)