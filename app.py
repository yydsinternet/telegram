from flask import Flask

# 创建 Flask 应用程序实例
app = Flask(__name__)

# 定义根路由处理逻辑
@app.route('/')
def index():
    return 'Welcome to my amazing app!'

# 导入 telebot 库
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your bot token
BOT_TOKEN = "6979924545:AAGxKlQTUmy8dnJL1J7h1kBw3rqWGCTh_Rg"

# Create a Telebot object
bot = telebot.TeleBot(BOT_TOKEN)

# Define message handler to respond to all messages
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # Your message handling logic here

# Define callback handlers for inline buttons
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    # Your callback handling logic here

# Start the bot
bot.polling()

# 在文件末尾添加以下代码，用于运行 Flask 应用程序
if __name__ == '__main__':
    app.run()
