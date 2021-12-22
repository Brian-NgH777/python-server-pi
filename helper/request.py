import requests
# import time
from requests.exceptions import HTTPError
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry

# requests.adapters.DEFAULT_RETRIES = 5
# session = requests.Session()
# session.keep_alive = False
# retry = Retry(connect=3, backoff_factor=0.5)
# adapter = HTTPAdapter(max_retries=retry)
# session.mount('http://', adapter)

timeout = 5

def Get(headers={}, url=""):
    if len(url) == 0:
        return 
    try:
        r = requests.get(url, headers=headers, timeout=timeout, auth=Authentication())
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return 
    except Exception as err:
        print(f'Other error occurred: {err}')
        return 

    return r

def Post(headers={}, url="", body={}):
    if len(url) == 0:
        return 
    try:
        r = requests.post(url, json=body, headers=headers, timeout=timeout, auth=Authentication())
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return 
    except Exception as err:
        print(f'Other error occurred: {err}')
        return

    return r

def PostFile(url="", path=""):
    if len(url) == 0 or len(path) == 0:
        return 
    try:
        files = {'file': open(path, 'rb')}
        # headers = {'Content-type': 'multipart/form-data'}
        r = requests.post(url, files=files)
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return 
    except Exception as err:
        print(f'Other error occurred: {err}')
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        return

    return r

def Authentication():
    auth= {
        "NoAuth": {},
        "Basic": HTTPBasicAuth("user", "password"),
        "Digest": HTTPDigestAuth("user", "password")
    }
    
    return auth["NoAuth"]