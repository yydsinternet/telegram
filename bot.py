import os
import json
import requests
from flask import Flask, request
from pyTelegramBotAPI import TeleBot
from pyTelegramBotAPI.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your bot token
BOT_TOKEN = "6979924545:AAGxKlQTUmy8dnJL1J7h1kBw3rqWGCTh_Rg"

# Replace with your Heroku app URL
HEROKU_APP_URL = "https://yyds-a6c415467569.herokuapp.com/"

# Create a Telebot object
bot = TeleBot(BOT_TOKEN)

# Start the Flask app
app = Flask(__name__)

# Define a message handler to respond to all messages
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # Get the chat ID and user ID from the message
    chat_id = message.chat.id

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

    # Send a message with inline keyboard
    bot.send_message(chat_id, f"[Welcome Zilli Shop!](https://www.zillishop.com/). You sent: {message.text}", reply_markup=keyboard, parse_mode='Markdown')

# Define callback handlers for inline buttons
@bot.callback_query_handler(func=lambda call: call.data == "check_order")
def check_order_callback(call):
    # Handle check order logic
    bot.send_message(call.message.chat.id, "Feature under development, stay tuned!")

@bot.callback_query_handler(func=lambda call: call.data == "contact_support")
def contact_support_callback(call):
    # Handle contact support logic
    bot.send_message(call.message.chat.id, "Our support team will get back to you soon. Please wait patiently.")

# Define the root route
@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello, World!'

# Define the webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    # Process POST request data
    update = TeleBot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "!", 200

# Set up webhook when the app is started
if __name__ == '__main__':
    # Remove any existing webhook
    bot.remove_webhook()
    
    # Set up the webhook
    webhook_url = f"{HEROKU_APP_URL}/webhook"
    response = requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={webhook_url}")
    
    # Check if webhook is set up successfully
    if response.status_code == 200:
        print("Webhook set up successfully!")
        try:
            # Send a message to notify if the webhook is set up successfully
            response = requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": "@zillishopbot", "text": "Webhook set up successfully!"})
            if response.status_code != 200:
                print("Failed to send notification message:", response.status_code)
        except Exception as e:
            print("Error sending notification message:", e)
    else:
        print("Failed to set up webhook:", response.status_code)

    # Run the Flask app
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
