import os
from flask import Flask, send_file
import random

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def imgTest():    
    random_img = random.randint(1, 5)
    return send_file(f"{random_img}.jpg")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 2027))
    app.run(host='0.0.0.0', port=port, debug=False)