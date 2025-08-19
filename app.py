from flask import Flask ,jsonify,render_template
from jwttoken import jwtretttoap
import os

app = Flask(__name__,template_folder='\')

@app.route('/')
def serve_html():
    # Render the ind.html file
    return render_template('index.html')
    
    
@app.route("/jwt/password=<string:pas>&uid=<int:userid>")
def jwtjson(pas,userid):
    jwt =jwtretttoap(passw=pas,uid=userid)
    if jwt == 0:
        data = {
            'Token': 'No Jwt Found',
            'credits': 'api'
        }
        return data
    else:
        data = {
            'Token': jwt,
            'credits': 'api'
        }
        return data
if __name__ == "__main__":
    app.run(debug=True)





