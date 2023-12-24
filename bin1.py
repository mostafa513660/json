import requests

def get_bin_info(message):
    bin_number = message.text.split()[1]  # Get the BIN number from user input
    if len(bin_number) < 6:
        return "𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗳𝗼𝗿𝗺𝗮𝘁! ❌"

    response = requests.get(f"https://lookup.binlist.net/{bin_number}")

    if response.status_code == 200:
        data = response.json()
        brand = data.get('brand', '------')
        card_type = data.get('type', '------')
        bin_num = bin_number[:6]
        country = data.get('country', {}).get('name', '------')
        flag = data.get('country', {}).get('emoji', '')
        bank_name = data.get('bank', {}).get('name', '------')
        country_code = data.get('country', {}).get('alpha2', '------')
        currency = data.get('country', {}).get('currency', '------')
        scheme = data.get('scheme', '------')
        full_name = message.from_user.first_name + " " + message.from_user.last_name if message.from_user.last_name else message.from_user.first_name

        message_response = f"✦━─ 𝓟𝓸𝓵𝓪𝓻𝓲𝓼 ─━✦\n\n"
        message_response += f"┌─➤ 𝓑𝓘𝓝 𝓘𝓷𝓯𝓸𝓻𝓶𝓪𝓽𝓲𝓸𝓷\n"
        message_response += f"├─ 𝓑𝓘𝓝 𝓝𝓾𝓶𝓫𝓮𝓻 : {bin_num}\n"
        message_response += f"├─ 𝓑𝓻𝓪𝓷𝓭 : {brand}\n"
        message_response += f"├─ 𝓣𝔂𝓹𝓮 : {card_type}\n"
        message_response += f"├─ 𝓑𝓪𝓷𝓴 : {bank_name}\n"
        message_response += f"├─ 𝓒𝓸𝓾𝓷𝓽𝓻𝔂 : {country} {flag}\n"
        message_response += f"├─ 𝓐𝓵𝓹𝓱𝓪 𝟮 𝓒𝓸𝓭𝓮 : {country_code}\n"
        message_response += f"├─ 𝓒𝓾𝓻𝓻𝓮𝓷𝓬𝔂 : {currency}\n"
        message_response += f"├─ 𝓢𝓬𝓱𝓮𝓶𝓮 : {scheme}\n"
        message_response += f"└─ 𝓑𝔂 : {full_name}\n"
        return message_response
    else:
        return "An error occurred while fetching BIN information." 