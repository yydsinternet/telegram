import json
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request # type: ignore

# 替换为您的机器人 token
BOT_TOKEN = "6979924545:AAGxKlQTUmy8dnJL1J7h1kBw3rqWGCTh_Rg"

# 创建 Telebot 对象
bot = telebot.TeleBot(BOT_TOKEN)

# 创建 Flask 应用
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

# 定义命令处理函数
@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="购物", url="https://www.zillishop.com")
    button2 = InlineKeyboardButton(text="查询订单", callback_data="check_order")
    button3 = InlineKeyboardButton(text="联系客服", callback_data="contact_support")
    keyboard.row(button1, button2)  # 修改后的行
    keyboard.row(button3)  

    bot.send_message(message.chat.id, "欢迎使用 Zilli Shop Bot！", reply_markup=keyboard)


    # 发送带按钮的消息
    bot.send_message(message.chat.id, "欢迎使用 Zilli Shop Bot！", reply_markup=keyboard)

# 定义回调处理函数
@bot.callback_query_handler(func=lambda call: call.data == "check_order")
def check_order_callback(call):
    # 处理查询订单逻辑
    bot.send_message(call.message.chat.id, "功能开发中，敬请期待！")

@bot.callback_query_handler(func=lambda call: call.data == "contact_support")
def contact_support_callback(call):
    # 处理联系客服逻辑
    bot.send_message(call.message.chat.id, "客服人员会尽快回复您，请耐心等待。")

# 启动 Flask 应用
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# 启动机器人
bot.polling()
