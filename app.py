from flask import Flask ,jsonify
from jwttoken import jwtretttoap
import os

app = Flask(__name__)

@app.route('/')
def serve_html():
    # Path to your HTML file
    html_file_path = 'improx.html'  # Replace with your actual file path
    
    # Check if file exists
    if not os.path.exists(html_file_path):
        return f"HTML file not found at: {html_file_path}"
    
    # Serve the HTML file
    return send_file(html_file_path)
    
    
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

