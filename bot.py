import os
from flask import Flask, request
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 获取Telegram Bot token
# BOT_TOKEN = os.environ.get('6979924545:AAGxKlQTUmy8dnJL1J7h1kBw3rqWGCTh_Rg')
# 修改成下面这样
BOT_TOKEN = "6979924545:AAGxKlQTUmy8dnJL1J7h1kBw3rqWGCTh_Rg"

# 创建 Telebot 实例
bot = telebot.TeleBot(6979924545:AAGxKlQTUmy8dnJL1J7h1kBw3rqWGCTh_Rg)

# 创建 Flask 应用程序实例
app = Flask(__name__)

# 定义根路由处理逻辑
@app.route('/')
def index():
    return 'Welcome to my zillishop!'

# 定义 Telegram webhook 路由
@app.route('/webhook', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return '', 200

# Define a message handler to respond to all messages
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # Get the chat ID and user ID from the message
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Send a reply message with an inline keyboard
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton(text="Home", url="https://www.zillishop.com/"),
        InlineKeyboardButton(text="Products", url="https://www.zillishop.com/products"),
        InlineKeyboardButton(text="Help", url="https://www.zillishop.com/help")
    )
    keyboard.row(
        InlineKeyboardButton(text="About Us", url="https://www.zillishop.com/about"),
        InlineKeyboardButton(text="Contact Us", url="https://www.zillishop.com/contact"),
        InlineKeyboardButton(text="FAQs", url="https://www.zillishop.com/faqs")
    )
    keyboard.row(
        InlineKeyboardButton(text="Shipping", url="https://www.zillishop.com/shipping"),
        InlineKeyboardButton(text="Returns", url="https://www.zillishop.com/returns"),
        InlineKeyboardButton(text="My Account", url="https://www.zillishop.com/myaccount")
    )
    keyboard.add(InlineKeyboardButton(text="Check Order", callback_data="check_order"))
    keyboard.add(InlineKeyboardButton(text="Contact Support", callback_data="contact_support"))

    # 修改这里的文本为链接
    bot.send_message(chat_id, f"<a href='https://www.zillishop.com/'>Hello from Zilli Shop!</a>. You sent: {message.text}", reply_markup=keyboard, parse_mode='HTML')

# Define callback handlers for inline buttons
@bot.callback_query_handler(func=lambda call: call.data == "check_order")
def check_order_callback(call):
    # Handle check order logic
    bot.send_message(call.message.chat.id, "Feature under development, stay tuned!")

@bot.callback_query_handler(func=lambda call: call.data == "contact_support")
def contact_support_callback(call):
    # Handle contact support logic
    bot.send_message(call.message.chat.id, "Our support team will get back to you soon. Please wait patiently.")

import os

# 获取Heroku提供的端口号，如果没有，则默认使用5000
port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    # 启动 Flask 应用程序，指定端口号为 Heroku 提供的端口号
    app.run(host='0.0.0.0', port=port)
