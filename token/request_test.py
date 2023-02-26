import base64
import requests


def padded_oracle_check(data):
    # form cookie text
    encoded = base64.b64encode(data).decode("utf-8")

    url = "http://mb0f0g.ctf.cc-sw.com"
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    }
    cookies = {"SESSIONID": encoded}
    r = requests.get(url, cookies=cookies, headers=headers)

    return b"You must log in to continue" not in r.content


if __name__ == "__main__":
    sample_data = b"ccswsux"
    padded_oracle_check(sample_data)
