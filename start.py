import telebot
import telebot.types

# 替换为您的机器人 token
BOT_TOKEN = "6979924545:AAGxKlQTUmy8dnJL1J7h1kBw3rqWGCTh_Rg"

# 创建 Telebot 对象
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    # 创建内联键盘按钮
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text="shopping", url="https://www.zillishop.com")
    keyboard.add(button)

    # 发送带按钮的消息
    bot.send_message(message.chat.id, "Welcome Zilli Shop Bot！", reply_markup=keyboard)

# 启动机器人
bot.polling()
