import json

@app.route('/webhook', methods=['POST'])
def webhook_handler():
    # 获取请求数据
    data = request.get_data()

    # 解析 JSON 数据
    try:
        update = json.loads(data.decode('utf-8'))
    except Exception as e:
        print("无法解析 JSON 数据:", e)
        return 'Invalid JSON', 400

    # 处理更新
    handle_update(update)

    # 返回成功响应
    return 'OK', 200
