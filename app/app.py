from flask import Flask
# import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola mundo desde flask"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
