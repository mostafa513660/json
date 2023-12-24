def get_id(message):
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.first_name + " " + message.from_user.last_name if message.from_user.last_name else message.from_user.first_name
    chat_id = message.chat.id

    response = "✦━─ 𝓟𝓸𝓵𝓪𝓻𝓲𝓼 ─━✦\n\n"
    response += "┌─➤ 𝓤𝓼𝓮𝓻 𝓘𝓷𝓯𝓸𝓻𝓶𝓪𝓽𝓲𝓸𝓷\n"
    response += "│\n"
    response += f"├─ 𝓤𝓼𝓮𝓻𝓷𝓪𝓶𝓮 : {username}\n"
    response += f"│\n"
    response += f"├─ 𝓕𝓾𝓵𝓵 𝓝𝓪𝓶𝓮 : {full_name}\n"
    response += f"│\n"
    response += f"├─ 𝓤𝓼𝓮𝓻 𝓘𝓭    : {user_id}\n"
    response += f"│\n"
    response += f"├─ 𝓒𝓱𝓪𝓽 𝓘𝓭  : {chat_id}\n"
    response += f"└─ 𝓑𝔂: {full_name}\n"

    return response