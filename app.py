from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Tech 𝐏𝐀𝐓𝐇𝐀𝐍 𝐒𝐈𝐑'


if __name__ == "__main__":
    app.run()
  
