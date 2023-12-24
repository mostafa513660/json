import random
import datetime
import re
import requests

def generate_cc(card_info):
    def multi_explode(delimiters, string):
        pattern = '|'.join(map(re.escape, delimiters))
        return re.split(pattern, string)

    def get_bin_info(bin_number):
        bin_info_url = f"https://lookup.binlist.net/{bin_number}"
        try:
            response = requests.get(bin_info_url)
            response.raise_for_status()
            bin_data = response.json()

            country_name = bin_data.get('country', {}).get('name', '⚠️')
            country_emoji = bin_data.get('country', {}).get('emoji', '')  # Extract emoji directly

            return {
                'card_type': bin_data.get('scheme', '⚠️'),
                'card_category': bin_data.get('type', '⚠️'),
                'card_brand': bin_data.get('brand', '⚠️'),
                'bank_name': bin_data.get('bank', {}).get('name', '⚠️'),
                'country': f"{country_name} {country_emoji}",
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching BIN info: {e}")
            return {}

    split_values = multi_explode([":", "|", "⋙", " ", "/"], card_info)

    bin_value = ''
    amount = 10

    exp_month = None
    exp_year = None

    if len(split_values) >= 1:
        bin_value = re.sub(r'[^0-9]', '', split_values[0])

    if len(split_values) >= 2:
        amount = int(re.sub(r'[^0-9]', '', split_values[1]))

    if len(split_values) >= 4:
        exp_month = re.sub(r'[^0-9]', '', split_values[2])
        exp_year = re.sub(r'[^0-9]', '', split_values[3])

    cards_data = f"BIN: {bin_value}\nAmount: {amount}\n\n"

    f = 0
    while f < amount:
        card_number, exp_m, exp_y, cvv = gen_card(bin_value, exp_month, exp_year)
        cards_data += f"{card_number}|{exp_m}|{exp_y}|{cvv}\n"
        f += 1

    bin_info = get_bin_info(bin_value)

    cards_data += f"\nCard Information: {bin_info.get('card_type', '⚠️')} - {bin_info.get('card_category', '⚠️')} - {bin_info.get('card_brand', '⚠️')}\n"
    cards_data += f"Bank: {bin_info.get('bank_name', '⚠️')}\n"
    cards_data += f"Country: {bin_info.get('country', '⚠️')}"

    return cards_data

def gen_card(bin, exp_month=None, exp_year=None):
    card_number = bin
    for _ in range(15 - len(bin)):
        digit = random.randint(0, 9)
        card_number += str(digit)
    digits = [int(x) for x in card_number]
    for i in range(0, 16, 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total = sum(digits)
    check_digit = (10 - (total % 10)) % 10
    card_number += str(check_digit)

    if exp_month:
        exp_m = str(int(exp_month)).zfill(2)
    else:
        exp_m = str(random.randint(1, 12)).zfill(2)
    
    if exp_year:
        exp_y = int(exp_year)
    else:
        current_year = datetime.datetime.now().year
        random_offset = random.randint(1, 5)
        exp_y = current_year + random_offset

    cvv = str(random.randint(0, 999)).zfill(3)

    return card_number, exp_m, exp_y, cvv