import requests
from requests.exceptions import HTTPError
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

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
        time.sleep(0.01)
        r = requests.post(url, files=files)
        r.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return 
    except Exception as err:
        print(f'Other error occurred: {err}')
        return

    return r

def Authentication():
    auth= {
        "NoAuth": {},
        "Basic": HTTPBasicAuth("user", "password"),
        "Digest": HTTPDigestAuth("user", "password")
    }
    
    return auth["NoAuth"]