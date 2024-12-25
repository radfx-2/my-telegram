SEND_CODE_HEADERS = {
    "Host": "my.telegram.org",
    "Content-Length": "24",
    "Sec-Ch-Ua-Platform": "Windows",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": '"Chromium";v="129", "Not=A?Brand";v="8"',
    "Sec-Ch-Ua-Mobile": "?0",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://my.telegram.org",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://my.telegram.org/auth",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=1, i"
}


SEND_PASSOWRD_HEADERS = {
    "Host": "my.telegram.org",
    "Content-Length": "76",
    "Sec-Ch-Ua-Platform": "Windows",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": '"Chromium";v="129", "Not=A?Brand";v="8"',
    "Sec-Ch-Ua-Mobile": "?0",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://my.telegram.org",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://my.telegram.org/auth",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=1, i"
}


APP_AUTH_HEADERS = {
    'Host': 'my.telegram.org',
    'Cookie': None,
    'Sec-Ch-Ua': '"Chromium";v="129", "Not=A?Brand";v="8"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Accept-Language': 'en-US,en;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://my.telegram.org/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Priority': 'u=0, i',
    'Connection': 'keep-alive'
}


CREATE_APP_HEADERS = { 
    'authority': 'my.telegram.org',
    'method': 'POST',
    'path': '/apps/create',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-length': '131',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': None,
    'origin': 'https://my.telegram.org',
    'pragma': 'no-cache',
    'referer': 'https://my.telegram.org/apps',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
}


# Exaption 
class ManyTries(Exception):
    """Sorry, too many tries. Please try again later . """

class CodeInvalid(Exception):
    """Invalid confirmation code!"""