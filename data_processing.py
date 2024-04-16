def handle_message(message):
    chat_id = message['chat']['id']
    text = message['text']

    # 根据消息内容执行 bot 逻辑
    if text == '/start':
        send_welcome_message(chat_id)
    elif text == '/help':
        send_help_message(chat_id)
    else:
        send_echo_message(chat_id, text)

def send_welcome_message(chat_id):
    # 使用 Telegram Bot API 发送欢迎消息
    bot.send_message(chat_id, "欢迎使用 Zilli Shop Bot!")

def send_help_message(chat_id):
    # 使用 Telegram Bot API 发送帮助消息
    bot.send_message(chat_id, "可以发送以下命令：\n/start - 开始使用\n/help - 获取帮助")

def send_echo_message(chat_id, text):
    # 使用 Telegram Bot API 回复用户消息
    bot.send_message(chat_id, "您发送了：" + text)

def handle_callback_query(callback_query):
    chat_id = callback_query['chat']['id']
    data = callback_query['data']

    # 根据按钮数据执行 bot 逻辑
    if data == 'check_order':
        check_order(chat_id)
    elif data == 'contact_support':
        contact_support(chat_id)

def check_order(chat_id):
    # 处理查看订单逻辑
    bot.send_message(chat_id, "功能开发中，敬请期待！")

def contact_support(chat_id):
    # 处理联系客服逻辑
    bot.send_message(chat_id, "我们的客服人员将尽快与您联系，请耐心等待。")
