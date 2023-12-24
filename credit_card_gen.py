import requests
from concurrent.futures import ThreadPoolExecutor
from cgen import cc_gen
import re

def is_luhn_valid(card_number):
    digits = [int(digit) for digit in card_number[::-1] if digit.isdigit()]
    checksum = sum(digits[0::2] + [sum(divmod(int(d) * 2, 10)) for d in digits[1::2]])
    return checksum % 10 == 0

def get_bin_info(bin_value):
    api_url = f"https://lookup.binlist.net/{bin_value}"
    response = requests.get(api_url)
    data = {}
    if response.status_code == 200:
        data = response.json()
    return data

def get_bin_info_parallel(bin_values):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(get_bin_info, bin_values))
    return results

def generate_cc(m, id, usertele):
    cards = ''
    text = m

    if len(text) < 6:
        return "𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗳𝗼𝗿𝗺𝗮𝘁! ❌"

    input = re.findall(r"[0-9]+", text)

    if len(input) == 0:
        return ''

    full_bin, mes, ano, cvv = 'x', 'x', 'x', 'x'

    if len(input[0]) >= 6:
        full_bin = input[0]

    if len(input) >= 2:
        mes = input[1]
    if len(input) >= 3:
        ano = input[2]
    if len(input) == 4:
        cvv = input[3]

    valid_ccs = []

    while len(valid_ccs) < 10:
        generated_cards = cc_gen(full_bin, mes, ano, cvv, amount=10)
        for card in generated_cards:
            if is_luhn_valid(card.split("|")[0]):
                valid_ccs.append(card)
            if len(valid_ccs) == 10:
                break

    cards = '\n'.join(valid_ccs)

    bin_info = get_bin_info_parallel([full_bin])[0]
    if bin_info:
        bin_info_text = f"""𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {bin_info.get('scheme', '------')} - {bin_info.get('type', '------')} - {bin_info.get('brand', '------')}
𝗕𝗮𝗻𝗸: {bin_info.get('bank', {}).get('name', '------')}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {bin_info.get('country', {}).get('name', '------')} {bin_info.get('country', {}).get('emoji', '------')} """
    else:
        bin_info_text = "𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗕𝗜𝗡! ❌"

    return f"""𝗕𝗜𝗡 ⇾ {full_bin}
𝗔𝗺𝗼𝘂𝗻𝘁 ⇾ 10

{cards}

{bin_info_text}
Checked By @{usertele} (<code>{id}</code>)
made by 《 <a href="t.me/z_nta">OWNER</a> 》"""