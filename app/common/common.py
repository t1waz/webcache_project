class RequestData:
    AVAILABLE_REQUEST_METHODS = ('get', 'post', 'delete', 'patch', 'put')
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'User-Agent': "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7;en-us) "
                      "AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17",
    }

    def __init__(self, url, method, headers, payload):
        is_valid, error = self.validate(url=url,
                                        payload=payload,
                                        method=method,
                                        headers=headers)
        if not is_valid:
            raise ValueError(error)

        self._url = url
        self._method = method
        self._headers = headers
        self._payload = payload

    @classmethod
    def validate(cls, url, method, headers, payload):
        if any(not isinstance(attribute, str) for attribute in (url, method)):
            return False, 'url and method must be string'

        if any(not isinstance(attribute, dict) for attribute in (headers, payload)):
            return False, 'headers and data must be dictionaries'

        if method.lower() not in cls.AVAILABLE_REQUEST_METHODS:
            return False, f'method must be in {cls.AVAILABLE_REQUEST_METHODS}'

        return True, None

    @property
    def session_call_arguments(self):
        session_call_arguments = {
            'url': self._url,
            'headers': {**self.HEADERS, **self._headers},
        }
        if self._method != 'get':
            session_call_arguments['data'] = self._payload

        return session_call_arguments

    @property
    def method(self):
        return self._method
