from flask import Flask ,jsonify
from jwttoken import jwtretttoap

app = Flask(__name__)
# str:n
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

