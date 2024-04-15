import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your bot token
BOT_TOKEN = "6979924545:AAGxKlQTUmy8dnJL1J7h1kBw3rqWGCTh_Rg"

# Create a Telebot object
bot = telebot.TeleBot(BOT_TOKEN)

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
    bot.send_message(chat_id, f"[Hello from Zilli Shop!](https://www.zillishop.com/). You sent: {message.text}", reply_markup=keyboard, parse_mode='Markdown')

# Define callback handlers for inline buttons
@bot.callback_query_handler(func=lambda call: call.data == "check_order")
def check_order_callback(call):
    # Handle check order logic
    bot.send_message(call.message.chat.id, "Feature under development, stay tuned!")

@bot.callback_query_handler(func=lambda call: call.data == "contact_support")
def contact_support_callback(call):
    # Handle contact support logic
    bot.send_message(call.message.chat.id, "Our support team will get back to you soon. Please wait patiently.")

# Start the bot
bot.polling()
