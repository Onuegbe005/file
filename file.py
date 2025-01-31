# coding:utf-8
#/usr/bin/python
#Cython++++()
import requests
import json
import subprocess
import zlib
import re
import time
import hashlib
import random
import string
import uuid
import base64
import os
mich = []
if len(mich) >= 1:
    print('edited')
else:
    pass
p = print
H = '\x1b[1;92m'
wit = '\033[1;92m'

COOKIE_FILE = "cookie.txt"





	
def File_():
    def generate_random_hash():
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=64))
        return hashlib.sha256(random_string.encode()).hexdigest()
    
    def get_headers_and_cookies(cookie, user_id, session_id):
        hashed_value = generate_random_hash()
        headers = {
    'User-Agent': 'Instagram 275.0.0.27.98 Android (33/13; 320dpi; 720x1438; Xiaomi/Redmi; 23106RN0DA; gale; mt6768; en_GB; 458229219)',
    # 'Accept-Encoding': 'zstd',
    'accept-language': 'en-GB, en-US',
    'authorization': f'Bearer IGT:2:{base64.b64encode(json.dumps({"ds_user_id": user_id, "sessionid": session_id}).encode()).decode()}',
    'ig-intended-user-id': None,
    'ig-u-ds-user-id': None,
    'ig-u-rur': 'CLN,71158224282,1765421481:01f7108de051375bf7059d59d3d37486e488b25a06a956ec9f462d06f6874596067c7583',
    'priority': 'u=3',
    'x-bloks-is-layout-rtl': 'false',
    'x-bloks-version-id': str(hashed_value),
    'x-fb-client-ip': 'True',
    'x-fb-connection-type': 'MOBILE.LTE',
    'x-fb-friendly-name': 'IgApi: friendships/26205010147/followers/_tail',
    'x-fb-request-analytics-tags': '{"network_tags":{"product":"567067343352427","purpose":"fetch","surface":"undefined","request_category":"api","retry_attempt":"0"}}',
    'x-ig-android-id': 'android-f5eebceb29a5b6cc',
    'x-ig-app-id': '567067343352427',
    'x-ig-app-locale': 'en_GB',
    'x-ig-bandwidth-speed-kbps': '1234.000',
    'x-ig-bandwidth-totalbytes-b': '2287076',
    'x-ig-bandwidth-totaltime-ms': '1468',
    'x-ig-client-endpoint': 'FollowListFragment:followers',
    'x-ig-capabilities': '3brTv10=',
    'x-ig-connection-type': 'MOBILE(LTE)',
    'x-ig-device-id': str(uuid.uuid4()),
    'x-ig-device-locale': 'en_GB',
    'x-ig-family-device-id': str(uuid.uuid4()),
    'x-ig-mapped-locale': 'en_GB',
    'x-ig-nav-chain': 'ExploreFragment:explore_popular:12:main_search:1733884911.791::,SingleSearchTypeaheadTabFragment:search_typeahead:13:button:1733884913.968::,ExploreFragment:explore_popular:14:search_result:1733884925.76::,SingleSearchTypeaheadTabFragment:search_typeahead:16:button:1733884931.283::,ExploreFragment:explore_popular:17:search_result:1733884948.127::,SingleSearchTypeaheadTabFragment:search_typeahead:19:button:1733884953.37::,UserDetailFragment:profile:20:search_result:1733884957.356::,ProfileMediaTabFragment:profile:21:button:1733884958.19::,FollowListFragment:followers:27:button:1733885469.923::',
    'x-ig-salt-logger-ids': '25624577,20119557,857816154,31784969,25952257,42991646',
    'x-ig-timezone-offset': '3600',
    'x-ig-www-claim': 'hmac.AR0N8KBBPm7AVdErbVRNNW6JLYZaP4zq0OljhW0ICDMi1Rqt',
    'x-mid': 'Zz8digABAAFzDWosRktUOBnZmwJM',
    'x-pigeon-rawclienttime': str(int(time.time())),
    'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-12',
    'x-tigon-is-retry': 'False',
    'x-fb-http-engine': 'MNS',
    'x-fb-rmd': 'state=URL_MODIFIED;v=1;ip=102.89.84.113;tts=1733885418;tkn=681c2d0882c5b4d84753277cb803b071;reqTime=54167;recvTime=54167;rn=APP_RESUME;if=Unknown;fbn=2;fbu=1;fbr=2',
}
        cookies = dict(item.split('=') for item in cookie.split('; '))
        return headers, cookies

    def save_cookie_to_file(cookie):
        with open(COOKIE_FILE, 'w') as file:
            file.write(cookie)

    def load_cookie_from_file():
        if os.path.exists(COOKIE_FILE):
            with open(COOKIE_FILE, 'r') as file:
                return file.read().strip()
        return None

    def handle_network_issues():
        print("[+] Network Issues")
        time.sleep(0)

    # Load existing cookie or prompt for a new one
    coki = load_cookie_from_file()
    if not coki:
        os.system('clear')
        p("_" * 70)
        print(f"""{H}
╔═══╗╔══╗╔╗───╔═══╗ 
║╔══╝╚╣╠╝║║───║╔══╝ 
║╚══╗─║║─║║───║╚══╗ 
║╔══╝─║║─║║─╔╗║╔══╝ 
║║───╔╣╠╗║╚═╝║║╚══╗ 
╚╝───╚══╝╚═══╝╚═══╝ 

╔══════════════════════════════════════════╗
║ Creator  : CHIGOZIEWORLDWIDE             ║
║ Github   : CHIG0ZIEWORLDWIDE             ║
║ WhatsApp : +2348069472717                ║
║ Version  : G.1                           ║
║ FILENAME : FILE                          ║
╚══════════════════════════════════════════╝

	""")
        coki = input('\033[1;92m[+] Input Cookie ')
        save_cookie_to_file(coki)
    
    link = input('\033[1;92m[+] Input User link ')
    file_path = input('\033[1;92m[+] Input file Name ')

    try:
        user_match = re.search('ds_user_id=(.*?);', coki)
        sesn_match = re.search('sessionid=(.*?);', coki)
        if not user_match or not sesn_match:
            print("Invalid cookie format.");os.system('rm -rf cookie.txt')
            return
        user = user_match.group(1)
        sesn = sesn_match.group(1)

        headers, cookies = get_headers_and_cookies(coki, user, sesn)

        print("\033[1;92m[+] Running ")
        response = requests.get(link, cookies=cookies, headers=headers)
        if response.status_code != 200:
            print("[+] Failed Cookie. Input New One ")
            os.remove(COOKIE_FILE)
            return

        match = re.search(r'"profile_id":"(\d+)"', response.text)
        if not match:
            print("\033[1;92m[+] Error Extracting Profile ID ")
            return
        profile_id = match.group(1)
        print(f"\033[1;92m[+] Successfully Dumped : Profile ID {profile_id}")

        base_url = f"https://i.instagram.com/api/v1/friendships/{profile_id}/followers/"
        next_max_id = None
        users_list = []

        while True:
            params = {
                "search_surface": "follow_list_page",
                "query": "",
                "enable_groups": "true",
                "rank_token": str(uuid.uuid4()),
            }
            if next_max_id:
                params["max_id"] = next_max_id
            
            try:
                response = requests.get(base_url, headers=headers, params=params)
                if response.status_code == 200:
                    try:
                        data = response.json()
                    except json.JSONDecodeError:
                        print("Invalid JSON response.")
                        break
                    
                    for user in data.get("users", []):
                        username = user["username"]
                        full_name = user["full_name"]
                        users_list.append(f'{username}|{full_name}')
                        with open(file_path, 'a') as file:
                            file.write(f'{username}|{full_name}\n')
                        print(f'\033[1;92m[+] Dumping {len(users_list)} | {username} | {full_name}')
                    next_max_id = data.get("next_max_id")
                    if not next_max_id:
                        break
                else:
                    print(f"\033[1;92m[+] Error Fetching Data : {response.status_code}")
                    break
            except requests.exceptions.RequestException:
                handle_network_issues()

    except Exception as e:
        print(f"\033[1;92m[+] error {e}")

File_()