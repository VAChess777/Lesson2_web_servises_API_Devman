import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(url, token):
    payload = {
        "long_url": url
    }
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks',
                             json=payload,
                             headers=headers)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(bitlink, token):
    payload = {
        'unit': 'month', 
        'units': '-1'
    }
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary',
        headers=headers,
        params=payload)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    return clicks_count


def is_bitlink(url, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url=f"https://api-ssl.bitly.com/v4/bitlinks/{url}",
                            headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser(
        description=
        "shortening URL in bitlink and displaying the number of clicks on the shortened link"
    )
    parser.add_argument(
        "url",
        help="use 'python main.py {url}'"
    )
    args = parser.parse_args()
    url = args.url
    url_components = urlparse(url)
    verified_url = f"{url_components.netloc}{url_components.path}"
    
    try:
        if is_bitlink(verified_url, token):
            clicks = count_clicks(verified_url, token)
            print(f"{url} количество переходов по ссылке: {clicks}")
        else:
            print('Битлинк', shorten_link(url, token))

    except requests.exceptions.HTTPError as error:
        print("Can't get data from server:\n{0}".format(error))


if __name__ == '__main__':

    main()

# ""https://translate.google.ru""
