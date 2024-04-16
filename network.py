def handle_update(update):
    update_id = update['update_id']
    message = update.get('message')
    callback_query = update.get('callback_query')

    # 根据消息类型处理
    if message:
        handle_message(message)
    elif callback_query:
        handle_callback_query(callback_query)
