from flask import Flask
import os
import telebot
import telebot.types

# 替换为您的机器人 token
BOT_TOKEN = "6979924545:AAGxKlQTUmy8dnJL1J7h1kBw3rqWGCTh_Rg"

# 创建 Telebot 对象
bot = telebot.TeleBot(BOT_TOKEN)

# 定义 Flask 应用
app = Flask(__name__)

# 定义路由，用于处理 Telegram bot 的回调
@app.route("/", methods=["POST"])
def handle_update():
    if update.content_type == "application/json":
        updates = json.loads(update.data.decode("utf-8"))
        for update in updates:
            message = telebot.types.Message(**update)
            bot.handle(message)
    return "OK"

# 定义启动 bot 的函数
def start_command(message):
    # 创建内联键盘按钮
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text="shopping", url="https://www.zillishop.com")
    keyboard.add(button)

    # 发送带按钮的消息
    bot.send_message(message.chat.id, "Welcome Zilli Shop Bot！", reply_markup=keyboard)

# 注册 start 命令处理函数
@bot.message_handler(commands=['start'])
def start_command(message):
    start_command(message)

# 启动 Flask 应用
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# 启动机器人
bot.polling()
