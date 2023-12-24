import requests

def get_ip(message):
    ip = message.text.split()[1]  # Get the IP address from user input
    url = f"http://ip-api.com/json/{ip}"  # API endpoint to get IP information
    response = requests.get(url).json()
    full_name = message.from_user.first_name + " " + message.from_user.last_name if message.from_user.last_name else message.from_user.first_name

    message_response = "✦━─ 𝓟𝓸𝓵𝓪𝓻𝓲𝓼 ─━✦\n\n"
    message_response += "┌─➤ 𝓘𝓟 𝓘𝓷𝓯𝓸𝓻𝓶𝓪𝓽𝓲𝓸𝓷\n"
    message_response += "│\n"
    message_response += f"├─ 𝓘𝓟 𝓐𝓭𝓭𝓻𝓮𝓼𝓼 : {response['query']}\n"
    message_response += f"│\n"
    message_response += f"├─ 𝓒𝓸𝓾𝓷𝓽𝓻𝔂 : {response['country']}\n"
    message_response += f"│\n"
    message_response += f"├─ 𝓡𝓮𝓰𝓲𝓸𝓷 : {response['regionName']}\n"
    message_response += f"│\n"
    message_response += f"├─ 𝓒𝓲𝓽𝔂 : {response['city']}\n"
    message_response += f"│\n"
    message_response += f"├─ 𝓛𝓪𝓽𝓲𝓽𝓾𝓭𝓮 : {response['lat']}, {response['lon']}\n"
    message_response += f"│\n"
    message_response += f"├─ 𝓙𝓸𝓲𝓷𝓮𝓭 : {response['isp']}\n"
    message_response += f"│\n"
    message_response += f"└─ 𝓑𝔂 : {full_name}\n"

    return message_response