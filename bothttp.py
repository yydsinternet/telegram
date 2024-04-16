import requests
import json

# 替换这里的BOT_TOKEN和HEROKU_APP_URL为你自己的值
BOT_TOKEN = "6979924545:AAGxKlQTUmy8dnJL1J7h1kBw3rqWGCTh_Rg"
HEROKU_APP_URL = "https://yyds-a6c415467569.herokuapp.com"  # 替换为你的Heroku应用的URL

# 构建请求的URL
url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={HEROKU_APP_URL}/webhook"

try:
    # 发送POST请求
    response = requests.post(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析 JSON 响应
        response_data = json.loads(response.text)
        if response_data["ok"]:
            print("Webhook 设置成功!")
        else:
            print("Webhook 设置失败:", response_data["error_code"], response_data["description"])
    else:
        print("请求失败:", response.status_code)
except Exception as e:
    print("发生异常:", e)
