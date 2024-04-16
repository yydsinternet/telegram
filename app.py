from flask import Flask

app = Flask(__name__)  # 创建 Flask 应用实例

# ... 您的路由和视图函数 ...

if __name__ == "__main__":
    app.run(debug=True)  # 启动应用程序
