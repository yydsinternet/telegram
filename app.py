from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

# 放在文件末尾，便于 Gunicorn 找到 
if __name__ == '__main__': 
    app.run()

