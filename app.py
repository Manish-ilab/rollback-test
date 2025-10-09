from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World – Version 4,This is a demo project demonstrating rollback"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
