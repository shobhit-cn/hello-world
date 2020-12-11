from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h3><b>This is a sample hello world file for Devspaces</b></h3>"

if __name__ == '__main__':
    app.run(debug=True,port=8000)