import re
import json

import furl
from bs4 import BeautifulSoup


def is_json_serializable(data_item):
    try:
        json.load(data_item)
        return True
    except ValueError:
        return False


class UrlService:
    CAPTCHA_PATTERN = 'https?://www.google.com/recaptcha/api.*'

    @classmethod
    def validate_url_item(cls, url_item):
        if isinstance(url_item, str):
            return True
        elif isinstance(url_item, list) and len(url_item) == 2:
            return all(is_json_serializable(value) for value in url_item)

        return False

    @classmethod
    def get_url_and_url_data(cls, url_item):
        if isinstance(url_item, str):
            return url_item, {}

        return url_item[0], json.loads(url_item[1])

    @classmethod
    def normalize_url(cls, url_item):
        if not cls.validate_url_item(url_item=url_item):
            raise ValueError('incorrect url item')

        url, url_data = cls.get_url_and_url_data(url_item=url_item)
        link = furl.furl(url.lower().strip().replace("https://", "http://"))

        return link.url, json.dumps(url_data, sort_keys=True).lower()

    @classmethod
    def has_captcha(cls, response):
        if isinstance(response, json.JSONEncoder):
            return False
        elif isinstance(response, BeautifulSoup):
            if any(re.match(cls.CAPTCHA_PATTERN, script_tag.get('src', ''))
                   for script_tag in response.find_all('script')):
                return True
            if any(re.match(cls.CAPTCHA_PATTERN, iframe_tag.get('src', ''))
                   for iframe_tag in response.find_all('iframe')):
                return True

        return False
